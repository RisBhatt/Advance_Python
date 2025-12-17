class Student:
    def __init__(self, name, marks):
        self.name = name
        self.roll_no = 101
        self.__marks = marks

    def display(self):
        print("Name: ", self.name)
        print("Roll No: ", self.roll_no)
        print("Marks: ", self.__marks)

stud = Student("Rishit", 95)
stud.display()