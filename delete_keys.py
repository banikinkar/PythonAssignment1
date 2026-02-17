"""
create a dictionary with sensitive information
write a program to delete the sensitive information
Validation message  if all sensitive information not available
"""
userinfo = { 'name': 'John',
             'email': 'johnkenedy@gmail.com',
             'password': 'Top@2026',
             'address': 'AmruthaSarovar,Belathur',
             'bank-account':'0104336789'
             }
print(userinfo)
sensitive_info = [ 'password','bank-account','phone']

for i in sensitive_info:
    if i in userinfo:
        print(f"{i} is sensitive")
        print(f"Deleted sensitive key : {i}, value : {userinfo[i]}")
        userinfo.pop(i)
    else:
        print(f"{i} is not present in userinfo,so can not delete")
print(userinfo)

