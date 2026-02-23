import json

students = {'student1':{'roll':101,'name':'John','percent':98.5,'sport':True},
            'student2':{'roll':108,'name':'Carol','percent':78.5,'sport':True},
            'student3':{'roll':91,'name':'Smith','percent':92,'sport':True},
            'student4':{'roll':50,'name':'Mona','percent':80,'sport':True},
            'student5':{'roll':78,'name':'Alex','percent':67,'sport':True}}
print(students)
print(type(students))

#dump() --> used to convert file for serialization
# with open("students_data.json","w") as fh:
#     json.dump(students,fh,indent=5)

#reading use load() ---> used to deserialisation

# with open("students_data.json","r") as fh:
#     json_data = json.load(fh)
#     print(json_data)
#     print(type(json_data))

###update() -->updates the dictionary data

with open('students_data.json', 'r') as fh:
    json_data=json.load(fh)
    # json_data.update({'student6':{'roll':101,'name':'John','percent':98.5,'sport':True}})
    json_data.update()

with open('students_data.json', 'w') as fh:
    json.dump(json_data, fh,indent=5)
    print(json_data)


