# Power BI Dashboard

An interactive three-page Power BI report exploring five semesters of
academic coaching appointment data and student evaluation outcomes at
the University of Missouri Learning Center.

Built using fully synthetic data — no real student or staff records
are included.

---

## Live HTML Versions

If you do not have Power BI Desktop installed, the same dashboards
are available as live web pages:

| Dashboard | Link |
|-----------|------|
| All Academic Coaching | [View live](https://hyperbyork.github.io/Portfolio/html/LC_AC_All_Interactive.html) |
| Level II Academic Coaching | [View live](https://hyperbyork.github.io/Portfolio/html/LC_LevelII_Interactive.html) |

---

## Files and Folder Structure
```
powerbi/
├── Learning.pbix          # Power BI report file
├── data/                  # Synthetic data files used by the report
└── screenshots/           # Preview images of each report page
```

---

## Opening the Report

1. Download [Power BI Desktop](https://powerbi.microsoft.com/desktop)
   — it is free
2. Download `Learning.pbix` from this folder
3. Open the file in Power BI Desktop
4. When prompted to locate the data source, point it to the `data/`
   subfolder in this directory
5. All visuals will refresh automatically once the path is updated

---

## Report Pages

**Page 1 — Overview**
Semester-by-semester attendance trends displayed as a combined bar
and line chart, session outcome breakdown, appointment type split
between Level II and regular AC, and delivery format.

**Page 2 — Topics and Engagement**
Coaching topic frequency, topic outcome stacking showing attended
versus cancelled versus no-show per topic, student demographics,
and college breakdown.

**Page 3 — Evaluations**
Student satisfaction scores by semester, per-dimension helpfulness
ratings across six coaching dimensions, class level and GPA
distribution of respondents, and referral source breakdown.

---

## Data

The `data/` subfolder contains all synthetic source files used
to build this report:

| File | Description | Rows |
|------|-------------|------|
| `appointments.csv` | Appointment records across five semesters | 2,132 |
| `evals_F25.xlsx` | Student evaluation responses — Fall 2025 | 31 |
| `evals_S25.xlsx` | Student evaluation responses — Spring 2025 | 107 |
| `college_major_lookup.csv` | Major code to college name reference | 35 |

All data was generated with Python using `numpy.random.seed(42)`
for full reproducibility. See the data folder README for complete
column documentation.

---

## Screenshots

The `screenshots/` subfolder contains preview images of each
report page for reference without opening Power BI Desktop.

---

## How It Was Built

**Data preparation — Power Query**
- Date and numeric columns cast to correct data types
- Custom `AC Type` column classifying appointments as Level II
  or Regular AC
- Custom `Delivery Format` column consolidating location types
  into SSC and Online
- Custom `Semester Sort` column enabling correct chronological
  ordering of semester labels
- Evaluation tables for S25 and F25 appended into a single
  combined table

**Data model**
- Many-to-one relationship between `appointments` and
  `college_major_lookup` on major code
- Evaluations table sits independently as a separate fact table

**DAX measures**
- `Total Sessions`, `Sessions Attended`, `Sessions Cancelled`,
  `Sessions No Show`
- `Attendance Rate` using `DIVIDE` to handle zero denominators
- `Avg Duration (Attended)` filtered to attended sessions only
- `Satisfaction Rate` and `Recommend Rate` on the evaluations table

**Theme**
Custom Mizzou-branded theme using Gold `#F1B82D` as the primary
data color and Black `#1C1A17` for headers and backgrounds.

---

## Tools

- Power BI Desktop
- Python and pandas for synthetic data generation
- NumPy random seed for reproducibility
