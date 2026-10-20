#session_timer.py
# Converts total session time in seconds into minutes and remaining seconds

total_seconds = input("Session length in seconds: ")

total_seconds = int(total_seconds)



time_in_minutes = total_seconds//60

time_in_seconds =total_seconds % 60 

print   (f"Session length: {time_in_minutes} minutes and {time_in_seconds} seconds")


# Test Outputs:
# Input 905: Session length: 15 minutes and 5 seconds
# Input 60:  Session length: 1 minutes and 0 seconds
# Input 59:  Session length: 0 minutes and 59 seconds


    