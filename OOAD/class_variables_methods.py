"""
class variables are defined at class level
same copy of class variables  shared among the objects

class methods are defined in class that are bound to class not to instance or objects
To create a class method a decorator called --> classmethod
"""
class Student:
    college_name="CET"
    department_name="mechanical Engg"

    def __init__(self,name,dept):
        print("calling the initializer method")
        print(f"inside init block self is {self}")
        self.name=name
        self.dept=dept

    def study(self,n_hours):
       print(f"self is :{self}")
       print(f"student study for {n_hours} a day")

    def sports(self,sports_name):
        print(f"student play :{sports_name}")

student1= Student("carol","science")
student2=Student("john","chemistry")

student1.grade="A"
student3=Student("Alice","Math")
# print(student1.__dict__)
# print(student2.__dict__)
# print(student3.__dict__)

# help(Student)

print(Student.department_name,student3.college_name,student1.department_name)



