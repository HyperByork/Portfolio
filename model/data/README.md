# Academic Coaching — Synthetic Dataset

Fully synthetic data generated to demonstrate the Academic Coaching 
dashboards in this portfolio. **No real student, coach, or institutional 
records are contained in these files.**

---

## Files

| File | Description | Rows |
|------|-------------|------|
| `appointments.csv` | Appointment records across 5 semesters | 2,132 |
| `evals_F25.xlsx` | Student evaluation responses — Fall 2025 | 31 |
| `evals_S25.xlsx` | Student evaluation responses — Spring 2025 | 107 |
| `college_major_lookup.csv` | Major code → College name reference table | 35 |

---

## How the data was generated

Each file was generated in Python using `numpy` and `pandas` with a fixed 
random seed (`np.random.seed(42)`) to ensure full reproducibility. 
Distributions were calibrated to match realistic patterns for a 
university academic coaching program:

- Semester volumes reflect typical fall/spring enrollment cycles, 
  with fall semesters carrying higher appointment loads
- Attendance rates fall between 62–71% per semester, consistent 
  with real program benchmarks
- Topic frequencies weight study habits, time management, and exam 
  preparation most heavily
- Coach workload follows a realistic distribution where a small number 
  of coaches carry the majority of sessions
- Student demographics (gender, race/ethnicity, first-generation status, 
  GPA range, class level) use proportions drawn from publicly available 
  higher education data
- Evaluation satisfaction scores and dimension ratings reflect 
  plausible outcomes for a high-performing student support program

---

## Semesters

| Code | Period |
|------|--------|
| F23 | Fall 2023 — Aug through Dec |
| S24 | Spring 2024 — Jan through May |
| F24 | Fall 2024 — Aug through Dec |
| S25 | Spring 2025 — Jan through May |
| F25 | Fall 2025 — Aug through Dec |

---

## Column reference

### appointments.csv

| Column | Type | Description |
|--------|------|-------------|
| `Date` | Date | Appointment date (YYYY-MM-DD) |
| `Semester` | Text | Semester code (e.g. F25) |
| `Provider` | Text | Coach code (Coach A – Coach AR) |
| `Appointment Type` | Text | Regular AC or Level II |
| `Reason` | Text | Coaching topic |
| `Attended Session` | Text | `yes`, `Cancelled`, or `no` |
| `Appointment Location Type` | Text | `OFFICE`, `ONLINE`, or `ELSEWHERE` |
| `Appointment Location Name` | Text | Room or platform name |
| `Scheduled Duration in Minutes` | Number | Scheduled session length |
| `Actual Duration in Minutes` | Number | Actual session length (attended only) |
| `Gender` | Text | Female / Male |
| `Race/Ethnicity` | Text | Standard IPEDS race/ethnicity codes |
| `First Generation Student` | Text | Yes / No |
| `Class Level` | Text | Freshman / Sophomore / Junior / Senior / Graduate Student |
| `Term GPA` | Text | GPA range bucket |
| `Primary Major` | Text | Major code (joins to `college_major_lookup.csv`) |
| `College` | Text | Academic college |
| `Services` | Text | Program tags |

### evals_F25.xlsx and evals_S25.xlsx

| Column | Description |
|--------|-------------|
| `Academic Coach Name:` | Coach code |
| `Submitted On` | Date evaluation was submitted |
| `Your Academic Level:` | Respondent class level |
| `Your Major:` | Respondent major code |
| `Your Current GPA:` | Respondent GPA range |
| `Where did you hear about the Academic Coaching program?` | Referral source |
| `Which Class?` | Class that assigned the appointment (if applicable) |
| `What did you and your Academic Coach work on?` | Topics covered (multi-select) |
| `Please rate your overall satisfaction...` | Overall satisfaction rating |
| `Would you recommend this program to someone else?` | Yes / No |
| Dimension columns (×7) | Helpfulness ratings across 7 coaching dimensions |

---

## Quick start
```python
import pandas as pd

# Load appointments
df = pd.read_csv('data/appointments.csv')

# Filter to Academic Coaching only
ac = df[df['Services'].str.contains('Learning Center Academic Coaching', na=False)]

# Filter to Level II only
lv2 = ac[ac['Appointment Type'].str.contains('Level II', na=False)]

# Join college lookup
lookup = pd.read_csv('data/college_major_lookup.csv')
merged = ac.merge(lookup, left_on='Primary Major', right_on='Major', how='left')

# Load and combine evaluations
evals = pd.concat([
    pd.read_excel('data/evals_S25.xlsx'),
    pd.read_excel('data/evals_F25.xlsx')
], ignore_index=True)
```

---

## Privacy note

This dataset was created specifically to avoid any privacy concerns 
while still producing a realistic and analytically useful dataset. 
It is safe to share publicly and use for demonstration, teaching, 
or portfolio purposes without restriction.
