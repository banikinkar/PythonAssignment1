"""
name= 'John'
age= 20
percentage =85.5

student = ['john',20,85.5]
print(student[-3],len(student))
days_of_week = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
print(f"last day of the week is {days_of_week[6]}")


##list operation

Slicing of list,concat,repeat,append,insert

s1= [3,4,7,9,23,11,34,45,60,90,20,19,27,31]
print(s1[::-1]) # reverse the list
print(s1[1:3])  # prints index 1 to position 3
print(s1[2:])   #prints 2nd position to end
print(s1[:4])   # prints till 4th position
print(s1[::5])
print(s1[1:0:])

# concat of list
l1 = [3,5,-3,'John']
l2 = [3.0,0,-2,1.11]
print(l1[1:2]+l2[::-2])
print(type(l1))
# repeat of list

print(l1*2)

#append of the list append()
fruits = ['apple','banana','mango']
fruits.append('jackfruit')
print(fruits)
#print(fruits.pop())
fruits.insert(1,'orange')
print(fruits)


## extend() remove() pop()

##append() only adds 1 element where as extend() can add multiple elements

fruits = ['apple','banana','mango']
fruits.extend(["orange","jackfruit","seasonal fruit"])
fruits.append([1,2])
print(fruits)

s1= [3,4,7,9,23,11,34,45,60,90,20,19,27,31]
print(s1.remove(45))
print(s1)

days_of_week = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
s1= [3,4,7,9,23,11,34,45,60,90,20,19,27,31]
days_of_week.reverse()
print(days_of_week)
print(days_of_week[::-1])
s1.sort()
print( s1) #sorts in ascending order
s1.sort(reverse=True) #sorts in descending order
print( s1)
"""
s1= [3,4,7,9,23,11,34,0,10,1,0,0,1,19,27,31]
print(f"The list is {s1}")
items_to_count = int(input("Enter the number to count from above list :"))
c1 = s1.count(items_to_count)
print(f"The occurrence of {items_to_count} in above list is : {c1}")

print("4"  in s1)  # checks strings so False




