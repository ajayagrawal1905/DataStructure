class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def display(self):
        print("Hi",self.name)
        print("Your Marks are:",self.marks)
    def grades(self):
        if self.marks >= 60:
            print("Youe got First Grade")
        elif self.marks >= 50:
            print("Youe got First Grade")
        elif self.marks >= 35:
            print("Youe got First Grade")
        else:
            print("You are Failed")

n = int(input("Enter Number of Student:"))
for i in range(n):
    name = input("Enter Name:")
    marks = int(input("Enter Marks"))
    s = Student(name,marks)
    s.display()
    s.grades()
    print()