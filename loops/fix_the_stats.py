# fix_the_stats.py
# Count failed logins and the average session length.
events = ["FAILED", "SUCCESS", "FAILED", "SUCCESS", "SUCCESS"]
minutes = [0, 30, 0, 15, 45]


# problem 1  failed counter was reset to 0 inside the loop; set it outside before the loop
failed = 0

for event in events:
    if event == "FAILED":
        failed += 1
print(f"Failed logins: {failed}")

total = 0
count = 0
for value in minutes:
    if value > 0:
        total += value
        count += 1
       
 #problem 2 print was inside the loop and integer division // was used
print(f"Average session: {total / count} minutes")



#problem 3 range(1, 4) stopped at 3 changed to range(1, 5)
for level in range(1, 5):
    print(f"Level {level}")