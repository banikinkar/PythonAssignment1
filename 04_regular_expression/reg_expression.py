# regular expression is RE module
import re
# message ="The current version is 3.13.Other previous version are 3.12,3.11,3.10"
#
# print(message.find("version"))
# print("version" in message)
# print(message[12])
#
# match_object=re.search( "version", message)
# print(match_object)
#
# #conditional
# if re.search("[13][.12]", message):
#     print("version match found")
# else:
#     print("version not match found")

# Learn Meta character , number pattern
# . matches character except new line character(\n)

# message_1 = "house house Address is 63/3, Bangalore-560047 ,flat-A204"
# address_found = re.search("[0-9][0-9].[,]", message_1)
# print(address_found)
# print(message_1[46])

# **learning r character in search
# \d any digit character \D anything but
#\s whitespace character

# s1="house house Address is 63/3, Bangalore-560047 ,flat-A204"
# pattern=r"[0-9][\d]"
# matchobj = re.search(pattern,s1)
# print(matchobj)



text = "House number 63, flat A204"
obj=re.findall(r"\d", text)
print(obj, type(obj))





