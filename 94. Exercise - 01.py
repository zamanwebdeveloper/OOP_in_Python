# Exercise - 01
class Student:
    versity = 'Dhaka International University'
    def __init__(self,name,subject,section):
        self.name = name
        self.subject = subject
        self.section = section
    def show(self):
        print('\nName = ',self.name,'\nSubject = ',self.subject,'\nSection = ',self.section,'\nVersity = ',self.versity)
first = Student(input('Enter Your Name = '),input('Enter Subject = '),input('Enter Section = '))
second = Student(input('Enter Your Name = '),input('Enter Subject = '),input('Enter Section = '))
third = Student(input('Enter Your Name = '),input('Enter Subject = '),input('Enter Section = '))
first.show()
second.show()
third.show()
