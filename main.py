import pandas as pd
import numpy as np

print("=" * 40)
print("STUDENT PERFORMANCE ANALYTICS SYSTEM")
print("=" * 40)

df = pd.read_csv("students.csv")

df["Total"] = df[["Math", "Science", "English"]].sum(axis=1)
df["Average"] = df[["Math", "Science", "English"]].mean(axis=1).round(2)

def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"

df["Grade"] = df["Average"].apply(calculate_grade)
df["Result"] = np.where(df["Average"] >= 40, "Pass", "Fail")

print("\nSTUDENT RESULTS")
print(df.to_string(index=False))

print("\nCLASS SUMMARY")
print("Total students:", len(df))
print("Class average:", round(df["Average"].mean(), 2))
print("Highest average:", df["Average"].max())
print("Lowest average:", df["Average"].min())
print("Students passed:", (df["Result"] == "Pass").sum())
print("Students failed:", (df["Result"] == "Fail").sum())

print("\nSUBJECT AVERAGES")
print(df[["Math", "Science", "English"]].mean().round(2))

print("\nATTENDANCE SUMMARY")
print("Average attendance:", round(df["Attendance"].mean(), 2), "%")
print("Students below 75% attendance:", (df["Attendance"] < 75).sum())

df.to_csv("student_results.csv", index=False)
print("\nResults saved to student_results.csv")

print("\nTOP 5 STUDENTS")
top_students = df.sort_values(
    by="Average", ascending=False
).head(5)
print(top_students[["Name", "Average", "Grade"]].to_string(index=False))

print("\nATTENDANCE ELIGIBILITY")
df["Attendance_Status"] = np.where(
    df["Attendance"] >= 75,
    "Eligible",
    "Low Attendance"
)
print(df[["Name", "Attendance", "Attendance_Status"]].to_string(index=False))

print("\nSUBJECT-WISE TOPPERS")
for subject in ["Math", "Science", "English"]:
    topper = df.loc[df[subject].idxmax()]
    print(f"{subject}: {topper['Name']} ({topper[subject]} marks)")
