import streamlit as st
from utils.ui_helper import score_ring_svg, score_color


def render_score(score_data):
    score_val = score_data["score"]
    col_ring, col_detail = st.columns([1, 2])

    with col_ring:
        st.markdown(score_ring_svg(score_val), unsafe_allow_html=True)

    with col_detail:
        st.markdown('<div class="section-header">Penalty breakdown</div>', unsafe_allow_html=True)

        if not score_data["penalties"]:
            st.markdown("""
            <div style="color:#22c55e;font-family:'IBM Plex Mono',monospace;
                        font-size:0.88rem;padding:1rem 0">
              No penalties — perfect score.
            </div>
            """, unsafe_allow_html=True)
        else:
            total_penalty = score_data["total_penalty"]
            for pen in score_data["penalties"]:
                bar_w = min(pen["applied_penalty"] / max(total_penalty, 1) * 100, 100)
                cap_hit = pen["applied_penalty"] < pen["raw_penalty"]
                cap_note = f' <span style="color:#334155;font-size:0.7rem">(capped from {pen["raw_penalty"]})</span>' if cap_hit else ""

                st.markdown(f"""
                <div style="margin-bottom:1rem">
                  <div style="display:flex;justify-content:space-between;margin-bottom:2px">
                    <span class="badge badge-rule">{pen['rule']}</span>
                    <span style="font-family:'IBM Plex Mono',monospace;font-size:0.82rem;
                                 color:#ef4444">−{pen['applied_penalty']}{cap_note}</span>
                  </div>
                  <div class="penalty-bar-bg">
                    <div class="penalty-bar-fill" style="width:{bar_w:.1f}%"></div>
                  </div>
                  <div style="font-size:0.68rem;color:#334155;margin-top:2px">
                    cap: {pen['cap']} pts
                  </div>
                </div>
                """, unsafe_allow_html=True)

        st.markdown(f"""
        <div style="border-top:1px solid #1e2330;padding-top:1rem;margin-top:0.5rem;
                    display:flex;justify-content:space-between">
          <span style="font-family:'IBM Plex Mono',monospace;font-size:0.78rem;color:#475569">
            TOTAL PENALTY
          </span>
          <span style="font-family:'IBM Plex Mono',monospace;font-size:0.88rem;color:#ef4444;font-weight:600">
            −{score_data['total_penalty']}
          </span>
        </div>
        <div style="display:flex;justify-content:space-between;margin-top:0.3rem">
          <span style="font-family:'IBM Plex Mono',monospace;font-size:0.78rem;color:#475569">
            FINAL SCORE
          </span>
          <span style="font-family:'IBM Plex Mono',monospace;font-size:0.88rem;
                       color:{score_color(score_val)};font-weight:600">
            {score_val} / 100
          </span>
        </div>
        """, unsafe_allow_html=True)