#
# I will update the code for the love of god stop asking 😭😭.
# I'll make it better and better the more I learn, this is an updatable (does that even exist?) project.
# Genuinely tired of comenting line for line while it not being useful at all so yes, summarizing!!
#




# Import some modules, for delays and opening links.
import time
import webbrowser


# Set both set_pwd and input_pwd as blank variables so the can easily be changed later.
set_pwd = ""
input_pwd = ""



# My first function!!!! Probably not so necessary but, I'm happy. Its only purpose is learning probably, besides of the main function of being able to call 6 lines of code with only login()-
def login():
    print("Welcome back!")
    time.sleep(0.6)
    global set_pwd
    print("Please input your password")
    global input_pwd
    input_pwd= input("Password: ")




# If "set_pwd" is blank (yes), prints some stuff and asks if you want to "create a new account" with a Y or N question, and if "Y" or "y" then create a new pwd and set it for "set_pwd"
if set_pwd == "":
    print("===========================")
    print("Do you want to create an account and set a new password?")
    print("This will overwrite the current one! (for this version)")
    time.sleep(1.5)
    print("Options: \n Yes (Y) \n No (N)")

    if input("Selected Option:") == "Y" or "y":
        set_pwd = input("New Password: ")
        login()
    else:
        exit()


# Soooo... while the input password when trying to login isn't the same as the one you set earlier it will say "Wrong!" and keep calling login function
while input_pwd != set_pwd:
    print("Wrong!")
    login()


# If the input password is the same as the one you set up earlier then print "Welcome back to your account!" and little silly prank (sorry)
if input_pwd == set_pwd:
    print("Welcome back to your account!")
    webbrowser.open("https://www.youtube.com/watch?v=xvFZjo5PgG0")              # I'm genuinely sorry, I'm disappointed in myself don't worry, I'll change it, someday.
