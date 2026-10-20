#session_timer.py
# Converts total session time in seconds into minutes and remaining seconds

total_seconds = input("Session length in seconds: ")

total_seconds = int(total_seconds)



time_in_minutes = total_seconds//60

time_in_seconds =total_seconds % 60 

print   (f"Session length: {time_in_minutes} minutes and {time_in_seconds} seconds")





    