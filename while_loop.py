"""
t1 = (1,2,3,4)
i =0
while i< len(t1):
    print(t1[i])
    i +=i+1
"""

current_password = "Python"
while True:
    User_password = input("Enter your password : ")
    if User_password == current_password:
        print("Login Successful!")
        break
    else:
        print("Wrong Password !! try again")

print("You are logged in")