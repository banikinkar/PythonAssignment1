import random
num = [2,3,4,6,7]
print(random.random())# float between 0.0 and 1.0
print(random.random())
print(random.randint(1,19)) # int between a & b
print(random.choice(num)) # used in sequence list

fruits = ["apple", "banana", "cherry"]
random.shuffle(fruits) # used in sequence list
print(fruits)
