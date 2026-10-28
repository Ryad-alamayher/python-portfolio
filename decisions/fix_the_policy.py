# fix_the_policy.py
# Check a new password against an example policy and classify its length.
MIN_LENGTH = 12

username = input("Username: ")
password = input("New password: ")

#syntax
#Forgetting the two point ( : )
if len(password) < MIN_LENGTH:
    print("- Too short.")

#semantic
#Changed `elif` to `if` so both checks can be executed independently 
if password == username:
    print("- Same as the username.")

if len(password) >= MIN_LENGTH:
    strength = "acceptable"
elif len(password) >= 16:
    strength = "long"
    
else:
    strength = "short"

#semantic
#Unindented the print line outside of `else` so it always printsx
print(f"Length: {len(password)} ({strength})")