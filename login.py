import time

saved_name = "Emmanuel"
saved_email = "emmanuelmanzoor02@gmail.com"
saved_username = "maniop"
# saved_password = "Maniop#125"

print("\t\t\t\t\t\tSign Up")

name = input("Enter your Name: ")

while True:
    email = input("Enter your email: ")
    if email == saved_email:
        print("This email is already synced")
    else:
        print("Email synced successfully")
        break

while True:
    username = input("Enter your username: ")
    if username == saved_username:
        print("username is unavailable")
    else:
        print("username is available")
        break

while True:
    password = input("Choose a strong password: ")
    if len(password) >= 8:
        break
    else:
        print("Password should be at least 8 characters long.")

while True:
    cnfrm_password = input("Confirm your password: ")
    if password == cnfrm_password:
        print("Password set successfully.")
        print("Everything is ok now login to view your profile")
        break
    else:
        print("Passwords do not match. Please try again.")

time.sleep(3)

print("\t\t\t\t\t\t Login")

while True:
    username_login = input("Enter your username: ")
    if username == username_login:
        print()
        break
    else:
        print("username did not found")
while True:
    password_login = input("Enter your password: ")
    if password == password_login:
        print("Login successful. Welcome to your profile!")
        break
    else:
        print("\nLogin failed. Please check your password.")

        