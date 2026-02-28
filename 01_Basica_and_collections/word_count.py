"""
Find the countries that name starts with "I" and print them in a list
"""
countries = ["India","Ireland","Pakistan","Iran","Iceland","Maldives","Indonesia","Singapore"]
count=0
output_list =[]
for i in countries:
    if i[0] =='I':
        count = count +1
        output_list.append(i)
print(f" Total number of countries with I are {count}")
print(f" Total number of countries with I are {output_list}")

