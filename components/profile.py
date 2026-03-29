import streamlit as st

def render_profile(df, profile):
    st.markdown('<div class="section-header">Raw data preview</div>', unsafe_allow_html=True)
    st.dataframe(df.head(20), use_container_width=True)

    st.markdown('<div class="section-header">Column profiles</div>', unsafe_allow_html=True)
    
    cols = st.columns(3)

    for i, (col, meta) in enumerate(profile["columns"].items()):
        missing_pct = meta["missing_pct"]
        bar_color    = "#ef4444" if missing_pct > 0.5 else ("#f59e0b" if missing_pct > 0.2 else "#38bdf8")
        accent_color = "#ef4444" if missing_pct > 0.5 else ("#f59e0b" if missing_pct > 0.2 else "#1e2330")
        has_numeric = "numeric" in meta and meta["numeric"]["mean"] is not None

        with cols[i % 3]:
            st.markdown(f"""
            <div class="sani-card">
                <span style="font-family:IBM Plex Mono,monospace;font-weight:900 font-size:1.9rem;color:rgb(130,243,255)">{col} :</span>
                <span style="font-family:IBM Plex Mono,monospace;font-size:0.65rem;color:rgb(255,180,120)">{meta['dtype']}</span>
                    <div class="col-stat">
                        <div class="s-val">{meta["missing"]}</div>
                        <div class="s-lbl">missing</div></div>
                    <div class="col-stat">
                        <div class="s-val">{missing_pct:.1%}</div>
                        <div class="s-lbl">missing %</div>
                        <div class="penalty-bar-bg" style="margin-top:4px">
                            <div class="penalty-bar-fill" style="width:{missing_pct*100:.1f}%;background:{bar_color}"></div>
                        </div></div>
                    <div class="col-stat">
                        <div class="s-val">{meta["unique"]}</div>
                        <div class="s-lbl">unique</div></div>
                </div>
            """, unsafe_allow_html=True)