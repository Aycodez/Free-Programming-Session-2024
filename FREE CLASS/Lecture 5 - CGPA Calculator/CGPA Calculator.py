import tkinter as tk


def calculate_cgpa():
    total_grade_points = 0
    total_credits = 0
    for i in range(num_courses):
        grade = grades_entry[i].get()
        credits = credits_entry[i].get()
        if grade.upper() == 'A':
            grade_points = 5.0

        elif grade.upper() == 'B':
            grade_points = 4.0

        elif grade.upper() == 'C':
            grade_points = 3.0

        elif grade.upper() == 'D':
            grade_points = 2.0
        elif grade.upper() == 'E':
            grade_points = 1.0
        elif grade.upper() == 'F':
            grade_points = 0.0
        else:
            cgpa_label.config(text="Invalid grade entered")
            return
        total_grade_points += grade_points * int(credits)
        total_credits += int(credits)
    cgpa = total_grade_points / total_credits
    cgpa_label.config(text="Your CGPA is: " + str(cgpa))


# GUI setup

root = tk.Tk()
root.title("CGPA Calculator")

num_courses = 7
grades_entry = []
credits_entry = []
courses_entry = []
for i in range(num_courses):
    course_label = tk.Label(root, text="Course " + str(i + 1) + ":")
    course_label.grid(row=i, column=0)
    courses_entry.append(tk.Entry(root))
    courses_entry[i].grid(row=i, column=1)
    grades_label = tk.Label(root, text="Grade " + str(i+1) + ":")
    grades_label.grid(row=i, column=2)
    grades_entry.append(tk.Entry(root))
    grades_entry[i].grid(row=i, column=3)
    credits_label = tk.Label(root, text="Credit unit :")
    credits_label.grid(row=i, column=4)
    credits_entry.append(tk.Entry(root))
    credits_entry[i].grid(row=i, column=5)

calculate_button = tk.Button(root, text="Calculate CGPA", command=calculate_cgpa)
calculate_button.grid(row=num_courses, column=0, columnspan=2)
cgpa_label = tk.Label(root)
cgpa_label.grid(row=num_courses, column=2, columnspan=2)

root.mainloop()
