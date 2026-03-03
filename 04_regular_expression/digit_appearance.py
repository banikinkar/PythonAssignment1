import re

r1=int(input("Enter a number: "))
r2=int(input("Enter another number: "))


numbers = list(range(r1, r2))
str_number=[str(num) for num in numbers]

count = 0
for num in str_number:
    matches = re.findall(r"2", num)
    count += len(matches)

print("Total occurrences of digit 2:", count)



