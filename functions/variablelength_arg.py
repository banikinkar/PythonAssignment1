#write a simple function with variable length argument and print result condition based

#########################################################
def example_arg_funct(*args):
    return args

print(example_arg_funct(3,4,5),type(example_arg_funct()))

#######################################################
def example_kwarg_funct(**args):
    return args

print(example_kwarg_funct(a=1,b=2,c=3),type(example_kwarg_funct()))
############################################################

def variable_length(student_name, student_id, *marks):
    if len(marks) == 0:
        print(f"{student_name} with sid:{student_id} has not appeared the exam")
        percent_marks = 0
    else :
        percent_marks = sum(marks) / len(marks)
        print(f"{student_name} with sid:{student_id}  scored totally {percent_marks}% marks")


### Example
variable_length("Alice", 45, 90,34,56,78,84)
variable_length("Julie", 12, 89,78,55,89,90)
variable_length("carol", 56, 89,23,45,45,98)
variable_length("Bob", 57)


