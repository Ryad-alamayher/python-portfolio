#login_decision.py
#A Login Decision

MAX_FAILED = 5
KNOWN_USER = "analyst"
STORED_PASSWORD = "Blue#Falcon72"

user_name = input("enter your Username : ")
failed_attempts = int(input("enter the Failed attempts : "))
password = input("enter your pass : ")

if failed_attempts >= MAX_FAILED:
    print("Account locked.")
elif user_name != KNOWN_USER:
    print("Unknown user.")
elif password != STORED_PASSWORD:
    print(f"Access denied. Attempts left:{MAX_FAILED-failed_attempts-1}")
else:
    print("Access granted.")

