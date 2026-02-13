import pandas as pd

grades = pd.Series([85, None, 92, 45, None, 78, 55])

missing_values = grades.isnull()

filled_grades = grades.fillna(0)

filtered_grades = filled_grades[filled_grades > 60]

print("Original Grades:\n")
print(grades)