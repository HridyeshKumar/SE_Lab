def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    else:
        return "Fail"

# Input
name = input("Enter Student Name: ")

mark1 = float(input("Enter Marks for Subject 1: "))
mark2 = float(input("Enter Marks for Subject 2: "))
mark3 = float(input("Enter Marks for Subject 3: "))

# Processing
total = mark1 + mark2 + mark3
average = total / 3

grade = calculate_grade(average)

# Output
print("\n------ Student Report ------")
print("Name     :", name)
print("Total    :", total)
print("Average  :", round(average, 2))
print("Grade    :", grade)