# fix_the_session.py
# This program reports a user's session time.
    
username = input("Username: ")

# Runtime Error fix: converted total_seconds from str to int using int()
total_seconds = int (input("Session length in seconds: "))

# Semantic Error fix: used integer division // instead of / to get whole minutes
minutes = total_seconds // 60
seconds = total_seconds % 60
 
   
print("=" * 30)
# Runtime Error fix: added f-string to properly format the variable
print(f"User: {username}")
# Semantic Error fix: converted minutes and seconds to strings to concatenate properly with text
print("Session: " + str(minutes) + " min " + str(seconds) + " s")
print("=" * 30)
