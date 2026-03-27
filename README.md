<div align="center">

<img src="https://img.shields.io/badge/Saniti-Fy-38bdf8?style=for-the-badge&labelColor=0f172a&color=38bdf8" alt="SanitiFy" height="40"/>

# Sanitify Dashboard

**Interactive data quality analysis and cleaning — powered by [Sanitify](https://github.com/Ashisheoran/sanitify)**

[![Live Demo](https://img.shields.io/badge/Live%20Demo-streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://sanitify.streamlit.app)
[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io)
[![sanitify](https://img.shields.io/badge/sanitify-v0.1.3-38bdf8?style=flat-square)](https://github.com/Ashisheoran/sanitify)
[![License: MIT](https://img.shields.io/badge/License-MIT-a855f7?style=flat-square)](LICENSE)

</div>

---

## 🌐 Live Demo

> Try it instantly — no installation required.

**[🚀 Open Dashboard → sanitify.streamlit.app](https://sanitify.streamlit.app)**

Upload your own CSV or explore one of the built-in sample datasets to see the full pipeline in action.

---

## Overview

**Sanitify Dashboard** is a production-quality Streamlit application that exposes the full power of the [Sanitify](https://github.com/Ashisheoran/sanitify) Python library through an intuitive visual interface.

It allows data engineers, ML engineers, and analysts to:

- Instantly **profile** any structured dataset
- **Detect** data quality issues using a rule-based validation engine
- View a transparent, **explainable quality score** (0–100)
- Explore **ML-assisted fix suggestions** with confidence ratings
- **Apply approved fixes** interactively and preview cleaned data
- **Export** a full structured JSON quality report

The dashboard is a thin, purposeful UI layer — all core logic (profiling, scoring, validation, cleaning) lives inside the [`sanitify`](https://github.com/Ashisheoran/sanitify) library.

---

## ✨ Features

| Feature | Description |
|---|---|
| **📊 Dataset Profiling** | Schema-aware column-level metadata: types, missing rates, cardinality, uniqueness |
| **⚠ Quality Validation** | Rule-based detection of high missing rates, constants, high cardinality, duplicate rows |
| **◔ Quality Score** | Weighted 0–100 score with full penalty breakdown — no black boxes |
| **✦ Suggested Fixes** | ML-assisted recommendations filtered by confidence threshold |
| **✅ Apply & Preview** | Approve individual fixes and instantly preview the cleaned DataFrame |
| **⤓ Export Report** | Download a full structured JSON report (profile + issues + score + suggestions) |
| **🗂 Sample Datasets** | Five built-in datasets for instant exploration without needing to upload files |
| **⚙ Configurable Settings** | Adjustable sample size cap and suggestion confidence threshold |

---

## 🖥 Dashboard Walkthrough

### Sidebar — Load Data & Configure

- Choose between **Upload CSV** and **Sample Dataset** modes
- Adjust the **max sample size** (up to 500,000 rows) for large-file performance
- Set a **suggestion confidence threshold** to filter fix quality

### Tabs — Explore Results

```
▣ Profile   →  Raw data preview + per-column metadata cards
⚠ Issues    →  Quality issue list with severity badges
◔ Score     →  Visual quality ring + penalty breakdown
✦ Fixes     →  Suggested fixes with per-fix approval checkboxes
⤓ Export    →  One-click JSON report download
```

### Metric Bar — At-a-Glance Health

Rows · Columns · Issues found · Duplicate rows · Quality score · Suggestions

---

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| **UI Framework** | [Streamlit](https://streamlit.io) |
| **Data Engine** | [Sanitify](https://github.com/Ashisheoran/sanitify) |
| **Data Manipulation** | [pandas](https://pandas.pydata.org) |
| **Language** | Python 3.9+ |

---

## ⚙ Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/Ashisheoran/Sanitify-Dashboard.git
cd Sanitify-Dashboard
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate      # macOS / Linux
.venv\Scripts\activate         # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the dashboard

```bash
streamlit run app.py
```

The app will open at **http://localhost:8501**.

---

## 📦 Dependencies

```
pandas==2.3.3
sanitify==0.1.3
streamlit==1.55.0
```

All core data quality logic is provided by [`sanitify`](https://github.com/Ashisheoran/sanitify). The dashboard itself adds no domain logic — it is purely a presentation layer.

---

## 🗂 Project Structure

```
Sanitify-Dashboard/
├── app.py                  # Entry point — page config, layout orchestration
├── requirements.txt        # Pinned dependencies
├── styles.css              # Custom dark-theme styling
│
├── components/             # Streamlit UI components (one per tab/section)
│   ├── sidebar.py          # File uploader, sample selector, settings
│   ├── landing.py          # Welcome screen (shown before data is loaded)
│   ├── metrics.py          # Top metric bar (rows, issues, score, etc.)
│   ├── profile.py          # Profile tab — raw preview + column cards
│   ├── quality.py          # Issues tab — rule violations with severity
│   ├── score.py            # Score tab — visual quality ring
│   ├── fixes.py            # Fixes tab — suggestions + apply workflow
│   └── export.py           # Export tab — JSON report download
│
└── utils/
    ├── analysis.py         # Wraps sanitify.DataCleaner calls
    └── ui_helper.py        # SVG helpers, badge renderers, CSS loader
```

---

## 🔗 Sanitify Library

This dashboard is the official visual interface for the **[Sanitify](https://github.com/Ashisheoran/sanitify)** Python library.

Sanitify provides:

- Structured dataset profiling
- Rule-based quality validation engine
- Explainable weighted quality scoring
- Deterministic cleaning utilities
- ML-assisted fix suggestions (human-in-the-loop)
- Structured JSON report export

```python
from sanitify import DataCleaner

dc = DataCleaner(df)

profile     = dc.profile()
issues      = dc.check_quality()
score       = dc.quality_score()
suggestions = dc.suggest_fixes(confidence_threshold=0.7)
clean_df    = dc.apply_fixes(approved_suggestions)
```

→ **[View Sanitify on GitHub](https://github.com/Ashisheoran/sanitify)**

---

## 🤝 Contributing

Contributions to the dashboard are welcome.

Before submitting a PR:

1. Ensure the app runs locally without errors (`streamlit run app.py`)
2. Keep UI components in `components/` and utility logic in `utils/`
3. Do not add domain logic to the dashboard — it belongs in [`sanitify`](https://github.com/Ashisheoran/sanitify)
4. Follow existing code style and component structure

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 👤 Author

**Ashish Sheoran**

- GitHub: [@Ashisheoran](https://github.com/Ashisheoran)
- Library: [github.com/Ashisheoran/sanitify](https://github.com/Ashisheoran/sanitify)
- Live Demo: [sanitify.streamlit.app](https://sanitify.streamlit.app)

---

<div align="center">
  <sub>Built with ❤️ using <a href="https://github.com/Ashisheoran/sanitify">Sanitify</a> and <a href="https://streamlit.io">Streamlit</a></sub>
</div>
