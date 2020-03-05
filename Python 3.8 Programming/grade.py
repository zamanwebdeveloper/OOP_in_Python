# Grade & Grade Point
print("Enter you subject mark : ")
mark = int(input())

if mark >= 80:
    if mark <= 100:
        print("Grade = A+\nGrade Point 4.00")
elif mark >= 75:
    if mark <= 79:
        print("Grade = A\nGrade Point 3.75")
elif mark >= 70:
    if mark <= 74:
        print("Grade = A-\nGrade Point 3.50")
elif mark >= 65:
    if mark <= 69:
        print("Grade = B+\nGrade Point 3.25")
elif mark >= 60:
    if mark <= 64:
        print("Grade = B\nGrade Point 3.00")
elif mark >= 55:
    if mark <= 59:
        print("Grade = B-\nGrade Point 2.75")
elif mark >= 50:
    if mark <= 54:
        print("Grade = C+\nGrade Point 2.50")
elif mark >= 45:
    if mark <= 49:
        print("Grade = C\nGrade Point 2.25")
elif mark >= 40:
    if mark <= 44:
        print("Grade = D\nGrade Point 2.00")
else:
    print("Fail")