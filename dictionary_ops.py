"""
groceries = {"milk":50,"eggs":40,"bread":10}
#print(groceries["milk"])
groceries["eggs"] = 10
groceries["daal"]=90
#print(groceries)


student1 = {"Maths":50,"Eng":80,"Physics":90,"Chemistry":60}
#print(student1["Physics"])
#print(student1["Oriya"])
#print(student1.get("Oriya"))

student1.update({"Eng":100})
#print(student1)

student_groceries = student1 | groceries
print(student_groceries)
#{'Maths': 50, 'Eng': 100, 'Physics': 90, 'Chemistry': 60, 'milk': 50, 'eggs': 10, 'bread': 10, 'daal': 90}
student_groceries.update({"Geology":0})
print(student_groceries)
"""


## not allowed : list, set, dict => mutable datatypes , so key in a dictionary can not be
## allowed : str,int,float,bool,tuple => immutable datatypes , so key in a dictionary can  be
d1 = {1.0: True, 2:False}
d2 = {(1,2,3): True, 2:False}
#print(d2)

# indexing inside dictionaries, find keys, find Values, find items

subject = {"Maths":50,"Eng":80,"Physics":90,"Chemistry":60,"Maths":80}
student2 ={'John': 15, 'Kapil': 14, 'Rohan': 16, 'Siva': 18, 'marks': {'Maths': 80, 'Eng': 80, 'Physics': 90, 'Chemistry': 60}}

#student1["marks"] = subject
#print(student1)
#print(student2['marks'][1])
##get function and pop function in dictionaries

student1 = {"name":"John" , "age":30, "subject":"Eng"}
#print(student1.get("percentage",90))
print(student1.keys(), student1.values())
print(student1.items(), student1.items())

###shalow copy, deep copy

l1= []




