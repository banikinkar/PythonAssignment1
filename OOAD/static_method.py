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

    @classmethod
    def music(cls,music_name):
        print(f"student music :{music_name}")

    @staticmethod
    def greet():
        print("Welcome to the class")

student1=Student("James",1)
student1.greet()





