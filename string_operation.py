"""
Find length of string
index in string(from left to right,right to left)
joining of string - concatenation
repetition operator in string
membership operation (in ,not in )
comparison  in python
removing spaces--strip()
replace() function
"""

s1 = 'Learning  python is fun'
s2 = 'java'
print(len(s1))
print(s1[3],s1[-2])
print(s2+s2)
print(s2 * 2)

print(s1.replace('python','java'))
print('python' in s1)
print('java' in s1)
print('bani' not in s2)

s3 = '          Learning  python is fun           '
print(s3)
print(s3.strip())


#count () upper() lower() title(), capitalize() startswith() endswith ()

x = 'we learning Python is fun . Good for KIDS'
y='Python'
print(x.count('is'))
print(f'Occurance of {y} in {x} is {x.count(y)}')
print(y.upper(),y.lower())
print(x.title())
print(x.capitalize())

v1 = "This is a Sunday"
print(v1.startswith('this'))
print(v1.endswith('Sunday'))


















