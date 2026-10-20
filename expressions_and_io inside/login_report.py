MAX_LOGIN_ATTEMPTS = 5

Username = input("Enter the your Username : ")

failed_attempts =int ( input("Enter the number of failed attempts : "))

attempts_are_left = MAX_LOGIN_ATTEMPTS - failed_attempts 

print("=" * 30)
print ("LOGIN REPORT")
print("=" * 30)


print (f"User:\t{Username}")
print (f"Failed:\t{failed_attempts}")
print (f"Attempts left:\t{attempts_are_left}")


