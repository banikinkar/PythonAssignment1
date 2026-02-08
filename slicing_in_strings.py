"""
s1 = "random string in Python"

type_s1 = s1[1:2:9]
print(s1[2])
print(s1[1:12:2])
print(type(type_s1))
"""

name = 'Bani'
age = '40'
subject = 'Science'
hours = 5

s1 ,s2,s3 = 30,40,30

print (name," is ", age," years old and he studies ",subject, hours," hours a day .")
print (f"{name}  is  {age}  years old and he studies  {subject} {hours}  hours a day .")
print(f"{name} scored total {s1+s2+s3} marks in all subjects.")


###reversing a string
v1 ="Banikinkar Pani"
print(v1[::-1])

"""
2. Common Slicing Shortcuts
You can omit any of the three parameters to use their default values: 
text[:stop]: From the beginning up to (but not including) stop.
text[start:]: From start until the end of the string.
text[:]: An exact copy of the whole string.
text[::step]: The whole string, but picking every n-th character. 
3. Negative Indexing
Python allows counting from the end of the string using negative numbers, where -1 is the last character. 
text[-3:]: Last three characters.
text[:-2]: All characters except the last two. 
4. Advanced Operations
Reversing a String: Use a negative step of -1 to reverse the sequence.
python
print("Python"[::-1]) # Output: 'nohtyP'
"""