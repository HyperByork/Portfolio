"""
Synthetic student course performance dataset.
Designed to support a full statistical modeling walkthrough:
  - Descriptive statistics and distributions
  - Hypothesis testing (t-test, ANOVA, chi-square)
  - Linear regression with assumption checking
  - Model diagnostics

Run from the project root:
    python model/generate_student_performance.py
"""

import numpy as np
import pandas as pd

np.random.seed(42)
N = 800

# ── Continuous predictors ──────────────────────────────────────────────────
prior_gpa = np.clip(np.random.normal(2.9, 0.7, N), 1.0, 4.0).round(2)

# Right-skewed: most students study 5–15 hrs/week, a few study much more
study_hours_per_week = np.clip(
    np.random.gamma(shape=2.5, scale=3.8, size=N), 0.5, 35.0
).round(1)

# Left-skewed: most students attend most classes
attendance_rate = np.clip(np.random.beta(8, 2, N), 0.35, 1.0).round(3)

# Zero-inflated: ~45% don't work, the rest work varying hours
work_flag = np.random.choice([0, 1], N, p=[0.45, 0.55])
part_time_work_hours = np.clip(
    work_flag * np.random.exponential(12, N), 0, 40
).round(1)

sleep_hours_per_night = np.clip(np.random.normal(6.8, 1.3, N), 4.0, 10.0).round(1)

# Lower-GPA students tend to attend more tutoring sessions
tutoring_base = np.clip(7 - 1.8 * prior_gpa + np.random.exponential(1.5, N), 0, 18)
tutoring_sessions = np.clip(tutoring_base, 0, 15).astype(int)

extracurricular_activities = np.random.choice(
    [0, 1, 2, 3, 4, 5], N, p=[0.15, 0.25, 0.30, 0.18, 0.08, 0.04]
)

# Anxiety: higher with more work hours, lower with higher GPA
anxiety_raw = (
    5.0
    + 0.09 * part_time_work_hours
    - 1.1 * (prior_gpa - 2.9)
    + np.random.normal(0, 1.5, N)
)
anxiety_score = np.clip(np.round(anxiety_raw), 1, 10).astype(float)

# ── Categorical predictors ─────────────────────────────────────────────────
semester = np.random.choice(["F23", "S24", "F24", "S25"], N)

# Section = instructor; A is slightly easier grader, C slightly harder
section = np.random.choice(["A", "B", "C"], N, p=[0.35, 0.35, 0.30])
section_effect = np.where(section == "A", 2.5, np.where(section == "B", 0.0, -2.5))

class_level = np.random.choice(
    ["Freshman", "Sophomore", "Junior", "Senior"], N, p=[0.35, 0.30, 0.20, 0.15]
)

first_gen_student = np.random.choice(["Yes", "No"], N, p=[0.30, 0.70])
major_type = np.random.choice(["STEM", "Non-STEM"], N, p=[0.40, 0.60])
age = np.clip(np.round(np.random.gamma(3, 2, N) + 17), 18, 30).astype(int)

# ── Outcome: final_score ───────────────────────────────────────────────────
# Known data-generating process (useful for checking how well models recover it):
#   final_score = 40 + 7.5*prior_gpa + 0.6*study_hours + 10*attendance_rate
#                 - 0.22*work_hours - 0.45*anxiety + 0.35*sleep + section + noise
final_score_raw = (
    40.0
    + 7.5  * prior_gpa
    + 0.60 * study_hours_per_week
    + 10.0 * attendance_rate
    - 0.22 * part_time_work_hours
    - 0.45 * anxiety_score
    + 0.35 * sleep_hours_per_night
    + section_effect
    + np.random.normal(0, 5, N)
)
final_score = np.clip(np.round(final_score_raw, 1), 30.0, 100.0)

letter_grade = np.select(
    [final_score >= 90, final_score >= 80, final_score >= 70, final_score >= 60],
    ["A", "B", "C", "D"],
    default="F",
)
passed = np.where(final_score >= 60, "Pass", "Fail")

# ── Introduce ~5 % missing values in self-reported columns ─────────────────
for arr, frac in [(anxiety_score, 0.05), (sleep_hours_per_night, 0.04)]:
    idx = np.random.choice(N, size=int(frac * N), replace=False)
    arr[idx] = np.nan

sleep_hours_per_night = sleep_hours_per_night.astype(float)

# ── Assemble DataFrame ─────────────────────────────────────────────────────
df = pd.DataFrame({
    "student_id":               [f"STU{str(i+1).zfill(4)}" for i in range(N)],
    "semester":                 semester,
    "course_section":           section,
    "age":                      age,
    "class_level":              class_level,
    "first_gen_student":        first_gen_student,
    "major_type":               major_type,
    "prior_gpa":                prior_gpa,
    "study_hours_per_week":     study_hours_per_week,
    "attendance_rate":          attendance_rate,
    "part_time_work_hours":     part_time_work_hours,
    "tutoring_sessions":        tutoring_sessions,
    "extracurricular_activities": extracurricular_activities,
    "sleep_hours_per_night":    sleep_hours_per_night,
    "anxiety_score":            anxiety_score,
    "final_score":              final_score,
    "letter_grade":             letter_grade,
    "passed":                   passed,
})

out_path = "model/data/student_performance.csv"
df.to_csv(out_path, index=False)

print(f"Saved {N} rows to {out_path}")
print(f"Columns: {list(df.columns)}")
print(f"Missing values:\n{df.isnull().sum()[df.isnull().sum() > 0]}")
print(f"\nOutcome summary:")
print(f"  final_score  mean={df.final_score.mean():.1f}  std={df.final_score.std():.1f}  "
      f"min={df.final_score.min()}  max={df.final_score.max()}")
print(f"  Pass rate: {(df.passed == 'Pass').mean():.1%}")
print(f"  Grade dist:\n{df.letter_grade.value_counts().sort_index()}")
