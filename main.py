import time


try:
    f = open("datos.txt", "x")
except FileExistsError:
    print("File already created, reading...")

def login():
    username_input = input("User: ")
    password_input = input("Password: ")

    with open("datos.txt", "r") as f:
        lines = f.readlines()

    # Recorremos en pasos de 2: una línea es el usuario, la siguiente es la contraseña
    for i in range(0, len(lines), 2):
        user = lines[i].strip()
        password = lines[i + 1].strip()
        if username_input == user and password_input == password:
            print("Login successful!")
            return

    print("Incorrect username or password.")
    time.sleep(1)
    login()


def create_account():
    user = input("Input the desired username: ")
    password = input("Enter the desired password: ")
    with open("datos.txt", "a") as fa:  # "fa" = file append
        fa.write(user + "\n")
        fa.write(password + "\n")
    print("Account created! You can login now.")
    time.sleep(1)
    login()


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

