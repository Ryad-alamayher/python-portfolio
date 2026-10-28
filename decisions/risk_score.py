#risk_score.py


score = 0 
risk_score=""

failed_attempts =int(input("enter the Failed attempts in the last hour : "))
login_hour =int(input("enter the Login hour (0-23) : "))
new_device =(input("New device (yes/no) : "))


if failed_attempts >= 3:
    score=score+40

if login_hour < 6:
    score=score+30

if new_device == "yes": 
    score=score+30


if score >= 70:
    risk_score = "HIGH"
elif score >=30:
    risk_score = "MEDIUM"
else:
    risk_score = "LOW"    



print (f"{failed_attempts},{login_hour},{new_device} Risk score: {score} ({risk_score}) ")