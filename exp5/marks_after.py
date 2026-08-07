SUBJECT_COUNT = 3

students = [
    ["Rahul", 80, 70, 90],
    ["Priya", 65, 75, 60],
    ["Aman", 90, 85, 88]
]

def calculate_total(marks):
    return sum(marks)

def calculate_average(total):
    return total / SUBJECT_COUNT

def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    return "Fail"

def print_student_report(student):
    name = student[0]
    marks = student[1:]

    total = calculate_total(marks)
    average = calculate_average(total)
    grade = calculate_grade(average)

    print(f"Name    : {name}")
    print(f"Total   : {total}")
    print(f"Average : {average:.2f}")
    print(f"Grade   : {grade}")
    print("-" * 30)

for student in students:
    print_student_report(student)