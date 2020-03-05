# Grade & Grade Point
print("Enter you subject mark : ")
mark = int(input())
if mark > 100:
    print("Please Enter Valid Subject Mark")
if mark >= 80:
    if mark <= 100:
        print("Grade = A+\nGrade Point 4.00") # 100 to 80
elif mark >= 75:
    if mark <= 79:
        print("Grade = A\nGrade Point 3.75") # 79 to 75
elif mark >= 70:
    if mark <= 74:
        print("Grade = A-\nGrade Point 3.50") # 74 to 70
elif mark >= 65:
    if mark <= 69:
        print("Grade = B+\nGrade Point 3.25") # 69 to 65
elif mark >= 60:
    if mark <= 64:
        print("Grade = B\nGrade Point 3.00") # 64 to 60
elif mark >= 55:
    if mark <= 59:
        print("Grade = B-\nGrade Point 2.75") # 59 to 55
elif mark >= 50:
    if mark <= 54:
        print("Grade = C+\nGrade Point 2.50") # 54 to 50
elif mark >= 45:
    if mark <= 49:
        print("Grade = C\nGrade Point 2.25") # 49 to 45
elif mark >= 40:
    if mark <= 44:
        print("Grade = D\nGrade Point 2.00") # 44 to 40
elif mark >= 0:
    if mark <= 43:
        print("Fail")
else:
    print("Please Enter Valid Subject Mark")
