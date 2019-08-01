import random
password=str(random.randint(100000,999999))
print("sing up")
fname=str(input("Hey user whats your first name? "))
lname=input("hey "+fname+" whats is your last name? ")
age=int(input("whats is your age? "))
if age<17:
    print("you cant sing up the age need to be 18!")
if age>119:
    for age in range(3):
        print("please enter vaild age!")
        age=int(input("whats is your age? "))
        if age<17:
            print("you cant sing up the age need to be 18!")
        if age<119:
            break;
if age<119 and age>17:
    print("hey "+fname+ " "+lname+" your new username is:")
    print(fname+lname)
    print("your password is:")
    print(fname+lname[0:2:2]+password)
    print("enjoy on our website!")
    username=fname+lname
    password=fname+lname[0:2:2]+password
    print("log in")
    logusername=str(input("hey user please enter your username: "))
    logpassword=str(input("hey "+logusername+ " please enter your password: "))
    while logusername!=username or logpassword!=password:
        print("The username or password you entered is incorrect")
        logusername=str(input("hey user please enter your username: "))
        logpassword=str(input("hey "+logusername+ " please enter your password: "))
        if logpassword==password and logusername==username:
            break;
if logpassword==password and logusername==username:
    print("log in sucsess")

