class Student:
    def __init__(self,name,rollno,grades):
        self.name = name
        self.rollno = rollno
        self.grades = grades

    def talk(self):
        print("Hello,My name is:",self.name)
        print("My Roll No.:",self.rollno)
        print("My Grades are:",self.grades)

s = Student('Ajay',19,'A')
s.talk()
s1 = Student('Dilasa',13,'A')
s1.talk()