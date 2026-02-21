def greeting_someone(name):
    print(f"hello {name} , How are you!\nAppreciate your time!")

## call function
greeting_someone('Bani')

def odd_even(number):
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

#call odd even function
odd_even(23)

def simple_sum(num1,num2):
    return num1 + num2

print(simple_sum(3,4))

"""
def multi_ops_function(num1,num2):
    add = num1+num2
    sub = num1-num2
    mult=num1*num2
    return add,sub,mult

val1=int(input("Enter first number: "))
val2=int(input("Enter second number: "))

rs1,rs2,rs3 = multi_ops_function(val1,val2)
print(f"Addition is {rs1}")
print(f"Subtraction is {rs2}")
print(f"Multiplication is {rs3}")
"""

def default_function(a,c=5,b=10):
    return a+b+c

# positional arguments **args ,goes only by position
print(default_function(6,8))
##Keyword arguments **kwargs  (specify the argument during call)
print(default_function(6,b=50))  ## example of **kwargs







