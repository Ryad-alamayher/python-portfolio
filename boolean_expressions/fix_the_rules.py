# fix_the_rules.py

# This program checks a connection against three rules.

role = input("Role: ")

port = int(input("Port: "))

is_admin = bool(role == "admin")

is_system_port = port <= 1023

is_web_port = bool(port == 80 or 443)

print(f"Admin: {is_admin}")

print(f"System port: {is_system_port}")

print(f"Web port: {is_web_port}")