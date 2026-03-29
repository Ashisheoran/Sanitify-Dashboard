import streamlit as st
from utils.ui_helper import severity_badge
from typing import Dict
def render_quality(issues):
    st.markdown('<div class="section-header">Detected issues</div>', unsafe_allow_html=True)

    if not issues:
        st.markdown("""
        <div class="sani-card sani-card-success" style="text-align:center;padding:2rem">
          <div style="font-family:'IBM Plex Mono',monospace;font-size:1.1rem;
                      color:#22c55e;margin-bottom:0.4rem">✓ No issues found</div>
          <div style="color:#475569;font-size:0.85rem">Your dataset passed all quality rules.</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        rule_counts: Dict[str, int] = {}
        for iss in issues:
            rule_counts[iss["rule"]] = rule_counts.get(iss["rule"], 0) + 1

        # Rule summary pills
        pills_html = "".join(
            f'<div class="metric-pill" style="min-width:90px">'
            f'<div class="val" style="font-size:1.1rem">{cnt}</div>'
            f'<div class="lbl">{rule}</div></div>'
            for rule, cnt in rule_counts.items()
        )
        st.markdown(f'<div class="metric-row">{pills_html}</div>', unsafe_allow_html=True)

        rows_html = ""
        for iss in issues:
            col_label = f'<span class="col-name">{iss["column"]}</span>' if iss["column"] else \
                        '<span class="col-name" style="color:#334155">— dataset level —</span>'
            metric_str = f'{iss["metric"]:.2%}' if isinstance(iss["metric"], float) else str(iss["metric"])
            threshold_str = f'{iss["threshold"]:.2%}' if isinstance(iss.get("threshold"), float) else "—"
            rows_html += f"""
            <div class="issue-row">
              {severity_badge(iss['severity'])}
              <span class="badge badge-rule">{iss['rule']}</span>
              <div style="flex:1">{col_label}</div>
              <div style="font-family:'IBM Plex Mono',monospace;font-size:0.78rem;color:#64748b">
                metric: {metric_str} &nbsp;|&nbsp; threshold: {threshold_str}
              </div>
            </div>"""

        st.markdown(f'<div class="sani-card">{rows_html}</div>', unsafe_allow_html=True)
