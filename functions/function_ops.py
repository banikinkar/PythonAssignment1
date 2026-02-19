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
