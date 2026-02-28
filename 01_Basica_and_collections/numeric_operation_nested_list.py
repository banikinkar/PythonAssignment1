"""
number = [1,3,4,5,6,7,8,9,23,34]
print(min(number),max(number))

total = sum(number)
print(total)
"""

##nested list
fruits = ['apple','banana','mango']
fruits.extend(["orange","jackfruit","seasonal fruit"])
fruits.append([1,2])
#print(fruits)


number = [1,3,4,5,6,7,8,[9,23,34]]
print(number[-1][-1])