user_input = input("Would you like to log in or close app?: ")
print("Please log in")
f = open("staff.txt", "r")
staff_data = f.read()
f.close()

for row in staff_data:
    field = row.split(",")
    username = str(field[0])
    user_password = str(field[0])
#user_input = input("Would you like to log in or close app?: ")
#print("Please log in")
while user_input == "log in":
    username = str(input("Enter your username: "))
    password = str(input("Enter your password: "))

    # for row in file:
    # field = row.split(",")
    # username = str(field[0])
    # password = str(field[1])
    if username == username and user_password == password:
        print("Log in successful!")
        break
    else:
        print("Wrong details. Please try again")
# f.close()
