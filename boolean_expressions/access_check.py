#access_check.py
#

MAX_FAILED = 5

role = bool (((input("Role : ")) == "admin") or ((input("Role : ")) == "root"))
mfa_passed = bool(input("MFA passed (yes/no): "))
failed_attempts = int(input("Failed attempts: "))


print (f"MFA OK: {mfa_passed}")
print (f"Privileged role: {role}") 
print (f"Can log in: {mfa_passed==True and failed_attempts < MAX_FAILED}")      