#write a simple function with variable length argument and print result condition based

print("#######################################################")
def example_arg_funct(*args):
    return args

print(example_arg_funct(3,4,5),type(example_arg_funct()))
print("#######################################################")
def example_kwarg_funct(**args):
    return args

print(example_kwarg_funct(a=1,b=2,c=3),type(example_kwarg_funct()))
print("#######################################################")

def variable_length(student_name, student_id, *marks):
    if len(marks) == 0:
        print(f"{student_name} with sid:{student_id} has not appeared the exam")

    else :
        percent_marks = sum(marks) / len(marks)
        print(f"{student_name} with sid:{student_id}  scored totally {percent_marks}% marks")


### input
variable_length("Alice", 45, 90,34,56,78,84)
variable_length("Julie", 12, 89,78,55,89,90)
variable_length("carol", 56, 89,23,45,45,98)
variable_length("Bob", 57)

print("#######################################################")

def student_details(sid, student_name, *extra, **marks):
    if len(marks) == 0:
        print(f"{student_name} with sid:{sid} has not appeared the exam")
    else :
       percentage=sum(marks.values()) / len(marks)
       print(f"Student {student_name} with ID: {sid} secured {percentage}% marks")
    print(f"Student {student_name} does extra activities like {extra}")

##input
student_details(23,"carol",'Debate','Singing',sub=1,sub2=79)
student_details(45,"john")

print("#######################################################")
