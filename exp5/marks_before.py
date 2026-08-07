students = [
    ["Rahul", 80, 70, 90],
    ["Priya", 65, 75, 60],
    ["Aman", 90, 85, 88]
]

for s in students:
    t = s[1] + s[2] + s[3]
    a = t / 3

    if a >= 90:
        g = "A+"
    elif a >= 80:
        g = "A"
    elif a >= 70:
        g = "B"
    elif a >= 60:
        g = "C"
    else:
        g = "Fail"

    print("Name:", s[0])
    print("Total:", t)
    print("Average:", a)
    print("Grade:", g)
    print("-------------------")