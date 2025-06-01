#
# This is my silly little prototype of a Login function
# It is DEFINETLY NOT SAFE as it is just made for understanding and learning things
#

# We import time because I like time.sleep()
import time


# We set a variable for the maximum times a user can try to login.
tries = 3


# Here we try to create a file called "datos.txt" and evade the error "FileExistsError", wich means a file with the same name is alredy created and it just throws an error
# because we are using the "x".
try:
    f = open("datos.txt", "x")
except FileExistsError:
    print("File already created, reading...")


# We define a function called login so we can reuse this code later
def login():
    global tries
    username_input = input("User: ")
    password_input = input("Password: ")

    with open("datos.txt", "r") as f:
        lines = f.readlines()

    # Pretty simple, if you ran out of tries then either you are stupid or idk man.
    if tries == 1:
        print("You have alredy tried too many times, try again later.")
        return

    for i in range(0, len(lines), 2):
        user = lines[i].strip()
        password = lines[i + 1].strip()
        if username_input == user and password_input == password:
            print("Login successful!")
            return
        else:
            # Every time you get either the username or password wrong it removes a chance and tells you how many you got left. And then recalls the function "login"
            print("Incorrect username or password.")
            tries -= 1
            print(f"You've got: {tries} tries left.")
            time.sleep(1)
            login()




# Another function! (I'm liking these) So we can reuse the code for "creating an account" every time we want, spoiler: in a few lines.
def create_account():
    user = input("Input the desired username: ")
    password = input("Enter the desired password: ")
    with open("datos.txt", "a") as fa:  # "fa" = file append
        fa.write(user + "\n")
        fa.write(password + "\n")
    print("Account created! You can login now.")
    time.sleep(1)
    login()

# With "datos.txt" (data in spanish I'm sorry for being spanish, damn) as "f", we read the content and if no user is found, you create another one, if there is then "login" 
with open("datos.txt", "r") as f:
    contenido = f.read().strip()
    if contenido == "":
        print("No user found, want to create a new one?")
        while True:
            response = input("Yes (Y) or No (N): ").strip().lower()
            if response == "y":
                create_account()
                break
            elif response == "n":
                login()
                break
            else:
                print("Invalid option, try again.")
    else:
        login()



#
# To-Do List
#

# Multiple users?
# Maybe just a little bit of encryption so you cannot just read the txt file?
# Optimizing? Hell nah I ain't doing none of that shit