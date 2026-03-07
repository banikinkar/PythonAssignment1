# # classes are bluprint or design of an objects
#  Object are entity created using class method
# Objects == instances of a class

class Student:

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
print(student1.name,student1.dept)
print(student2.name,student2.dept)
student3=Student("Alice","Math")
print(student1.__dict__)
print(student2.__dict__)
print(student3.__dict__)

