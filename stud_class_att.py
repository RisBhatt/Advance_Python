# Define the Student class
class Student:
    def __init__(self, name, roll_no, age, course):
        self.name = name
        self.roll_no = roll_no
        self.age = age
        self.course = course

    def print_details(self):
        print(f"Name   : {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Age    : {self.age}")
        print(f"Course : {self.course}")
        print("-" * 20)


# Create 2 Student objects
student1 = Student("ABC", 101, 20, "Computer Science")
student2 = Student("XYZ", 102, 21, "Artificial Intelligence")

# Print student details
student1.print_details()
student2.print_details()
