#This module contains the logic of the application without connectivity to a database.

print (" Blackgeek Login System")
#Menu
print(" ** Select an Option Below **")
choice = int(input(" 1. Register \n 2. Login \n 3. Exit \n: "))

#variable
setUsername ="admin"
setPassword ="1234"

#function to register user
def userRegister(username, password):
  print("User Registered")

#function for user login
def userLogin():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if (username!=setUsername):
        print("ERR:: Login Credetials incorrect")
    elif (password != setPassword):
        print("ERR:: Login Credetials incorrect")
    else:
        print("Login Successful !!")


#main
if (choice == 1):
    setUsername = str(input("Set username: "))
    setPassword = str(input("Set Password: "))
    userRegister(setUsername, setPassword)
elif (choice == 2):
    userLogin()
elif (choice == 3):
    print("Exited Successfully...")
else:
    print("ERR:: Option incorrect")

