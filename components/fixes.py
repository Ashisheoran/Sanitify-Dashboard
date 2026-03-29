import streamlit as st
from sanitify import DataCleaner

def render_fixes(df, suggestions):
    st.markdown('<div class="section-header">Suggested fixes</div>', unsafe_allow_html=True)

    if not suggestions:
        st.markdown("""
        <div class="sani-card" style="text-align:center;padding:2rem">
          <div style="color:#475569;font-size:0.88rem">
            No suggestions at the current confidence threshold.<br>
            Lower the slider in the sidebar to see more.
          </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        approved_indices = []

        for i, sug in enumerate(suggestions):
            conf_color = "#22c55e" if sug["confidence"] >= 0.85 else (
                "#f59e0b" if sug["confidence"] >= 0.7 else "#ef4444"
            )
            col_label = sug["column"] or "— dataset level —"

            st.markdown(f"""
            <div class="sani-card" style="margin-bottom:0.5rem">
              <div style="display:flex;align-items:center;gap:0.75rem;margin-bottom:0.4rem">
                <span class="badge badge-op">{sug['operation']}</span>
                <span class="col-name">{col_label}</span>
                <div style="flex:1"></div>
                <span style="font-family:'IBM Plex Mono',monospace;font-size:0.72rem;
                             color:{conf_color}">
                  {sug['confidence']:.0%} conf.
                </span>
              </div>
              <div style="font-size:0.8rem;color:#475569">{sug['reason']}</div>
            </div>
            """, unsafe_allow_html=True)

            approved = st.checkbox(f"Approve", key=f"fix_{i}", value=True)
            if approved:
                approved_indices.append(i)

        st.markdown("<br>", unsafe_allow_html=True)

        if st.button("⟳  Apply approved fixes", type="primary"):
            approved_fixes = [suggestions[i] for i in approved_indices]
            if not approved_fixes:
                st.warning("No fixes approved.")
            else:
                try:
                    dc = DataCleaner(df)
                    clean_df = dc.apply_fixes(approved_fixes)

                    st.markdown('<div class="section-header">Cleaned DataFrame preview</div>',
                                unsafe_allow_html=True)

                    col_before, col_after = st.columns(2)
                    with col_before:
                        st.markdown(
                            '<div style="font-family:IBM Plex Mono,monospace;font-size:0.7rem;'
                            'letter-spacing:0.1em;color:#334155;text-transform:uppercase;'
                            'margin-bottom:0.3rem">Before</div>',
                            unsafe_allow_html=True,
                        )
                        st.dataframe(df, use_container_width=True, height=200)
                        st.caption(f"{df.shape[0]} rows × {df.shape[1]} cols")

                    with col_after:
                        st.markdown(
                            '<div style="font-family:IBM Plex Mono,monospace;font-size:0.7rem;'
                            'letter-spacing:0.1em;color:#22c55e;text-transform:uppercase;'
                            'margin-bottom:0.3rem">After</div>',
                            unsafe_allow_html=True,
                        )
                        st.dataframe(clean_df, use_container_width=True, height=200)
                        st.caption(f"{clean_df.shape[0]} rows × {clean_df.shape[1]} cols")

                    # Download cleaned CSV
                    csv_bytes = clean_df.to_csv(index=False).encode()
                    st.download_button(
                        "↓  Download cleaned CSV",
                        data=csv_bytes,
                        file_name="cleaned_data.csv",
                        mime="text/csv",
                    )
                    st.session_state["clean_df"] = clean_df

                except Exception as exc:
                    st.exception(exc)
