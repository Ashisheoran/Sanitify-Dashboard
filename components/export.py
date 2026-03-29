import streamlit as st
import json

def render_export(profile, issues, score, suggestions):
    st.markdown('<div class="section-header">Export report</div>', unsafe_allow_html=True)

    report = {
        "profile": profile,
        "quality_issues": issues,
        "quality_score": score,
        "suggested_fixes": suggestions,
    }

    report_json = json.dumps(report, indent=2)

    col_left, col_right = st.columns([2, 1])

    with col_left:
        st.markdown("""
        <div class="sani-card sani-card-accent">
          <div style="font-size:0.68rem;letter-spacing:0.14em;text-transform:uppercase;
                      color:#475569;margin-bottom:0.75rem">JSON Report</div>
        """, unsafe_allow_html=True)

        st.download_button(
            "↓  Download report.json",
            data=report_json.encode(),
            file_name="sanitipy_report.json",
            mime="application/json",
        )

        st.markdown("</div>", unsafe_allow_html=True)

        with st.expander("Preview JSON"):
            st.code(report_json[:3000] + ("\n…truncated" if len(report_json) > 3000 else ""),
                    language="json")

    with col_right:
        st.markdown(f"""
        <div class="sani-card">
          <div class="section-header" style="margin-top:0">Report contents</div>
          <div class="issue-row">
            <span style="font-family:'IBM Plex Mono',monospace;font-size:0.8rem;
                         color:#38bdf8">profile</span>
            <span style="color:#475569;font-size:0.78rem">{profile["dataset"]["columns"]} columns</span>
          </div>
          <div class="issue-row">
            <span style="font-family:'IBM Plex Mono',monospace;font-size:0.8rem;
                         color:#38bdf8">quality_issues</span>
            <span style="color:#475569;font-size:0.78rem">{len(issues)} items</span>
          </div>
          <div class="issue-row">
            <span style="font-family:'IBM Plex Mono',monospace;font-size:0.8rem;
                         color:#38bdf8">quality_score</span>
            <span style="color:#475569;font-size:0.78rem">{score['score']} / 100</span>
          </div>
          <div class="issue-row">
            <span style="font-family:'IBM Plex Mono',monospace;font-size:0.8rem;
                         color:#38bdf8">suggested_fixes</span>
            <span style="color:#475569;font-size:0.78rem">{len(suggestions)} items</span>
          </div>
        </div>
        """, unsafe_allow_html=True)

        if "clean_df" in st.session_state:
            st.markdown("""
            <div class="sani-card sani-card-success" style="margin-top:1rem">
              <div style="font-size:0.68rem;letter-spacing:0.14em;text-transform:uppercase;
                          color:#22c55e;margin-bottom:0.4rem">Cleaned DataFrame</div>
              <div style="font-size:0.78rem;color:#475569">Available for download in the Fix tab.</div>
            </div>
            """, unsafe_allow_html=True)