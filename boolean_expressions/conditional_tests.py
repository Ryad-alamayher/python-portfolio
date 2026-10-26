#conditional_tests.py

user = "analyst"
role = "viewer"
failed = 3
port = 22

#True
print("Is failed >= 3? I predict True.")
print(failed >= 3)

print("\nIs user == \"analyst\" ? I predict True")
print(user == "analyst")

print("\nIs (port>=failed) ^ (failed >= port) ? I predict True ")
print((port>=failed) ^ (failed >= port))

print("\nIs failed<=port ? I predict True")
print(failed<=port)

print("\nIs role=\"viewer\" ? I predict True ")
print(role=="viewer" or failed<=port)


#False
print("\nIs user == \"analyst\" ? I predict False")
print(user != "analyst")

print("\nIs user == role ? I predict False")
print(user == role)

print("\nIs failed >= port ? I predict False")
print(failed >= port and user != role)

print("\nIs failed == user ? I predict False")
print(failed == user)

print("\nIs port//failed <= failed ? I predict False")
print(port//failed <= failed)