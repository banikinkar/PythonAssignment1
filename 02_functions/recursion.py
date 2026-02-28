## factorial of a number

def fact_rec(num):

    if num == 0:
        return 1
    else:
        return num * fact_rec(num-1)

print(fact_rec(5))


def add(num):
    num +=1
    return num

def square(num):
     num =num**2
     return num

print(square(add(3)))


