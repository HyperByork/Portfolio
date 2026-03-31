
# HTML Dashboards

Two interactive dashboards built with vanilla HTML, CSS, and JavaScript
exploring five semesters of academic coaching appointment data and student
evaluation outcomes at the University of Missouri Learning Center.

No frameworks, no build tools, no installation — each dashboard is a
single self-contained file that opens in any modern browser.

---

## Live Links

| Dashboard | Description | Link |
|-----------|-------------|------|
| All Academic Coaching | Program-wide view across all appointment types and five semesters | [View live](https://hyperbyork.github.io/Portfolio/html/LC_AC_All_Interactive.html) |
| Level II Academic Coaching | Deep dive into the Level II coaching program with evaluation data | [View live](https://hyperbyork.github.io/Portfolio/html/LC_LevelII_Interactive.html) |

---

## Files

| File | Description |
|------|-------------|
| `LC_AC_All_Interactive.html` | Program-wide dashboard — all AC appointments |
| `LC_LevelII_Interactive.html` | Level II-specific dashboard including student evaluations |

---

## Dashboard Features

### All Academic Coaching

- Semester selector that filters all panels simultaneously
- Attended sessions and attendance rate shown as a combined bar and line chart
- Session outcome breakdown — attended, cancelled, and no-show
- Appointment type split — Level II vs. regular AC stacked by semester
- Coaching topic frequency with outcome stacking per topic
- Student engagement metrics — unique students, average visits, and repeat rate
- College breakdown from joined roster data
- Student evaluation satisfaction scores and per-dimension helpfulness ratings

### Level II Academic Coaching

- Same semester navigation and combined attendance trend chart
- Level II-specific topic breakdown and outcome stacking
- Repeat visit analysis — visit frequency distribution by semester
- Student evaluation section with satisfaction scores, per-dimension
  helpfulness ratings, class level, GPA distribution, and referral sources

---

## How It Was Built

Each dashboard is a single HTML file. No external files are required
at runtime — all data is embedded directly in the JavaScript.

**Structure:** Semantic HTML with a fixed header, semester navigation
bar, KPI stat cards, and a CSS grid panel layout.

**Styling:** Plain CSS using Mizzou brand colors — Gold `#F1B82D`
and Black `#1C1A17`. No CSS frameworks.

**Charts:** Chart.js (loaded from CDN) powers the combined bar and
line attendance chart and the stacked appointment type chart.
All other visuals — horizontal bar charts, stacked segment bars,
and outcome breakdowns — are built with pure CSS.

**Interactivity:** Vanilla JavaScript. Clicking a semester button
swaps pre-computed data objects into every panel and rebuilds
Chart.js instances simultaneously.

---

## Running Locally

1. Download `LC_AC_All_Interactive.html` or `LC_LevelII_Interactive.html`
2. Open the file in Chrome, Firefox, Safari, or Edge
3. No setup required

---

## Data Note

Both dashboards use fully synthetic data generated with Python to match
realistic distributions for a university academic coaching program.
No real student or staff records are included. See the `powerbi/data/`
folder for the source files and full documentation.
