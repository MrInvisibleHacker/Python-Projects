def evaluate_vulnerability(bug_name):
    if bug_name == "sqli" or bug_name == "rce":
         return "Critical"
    elif bug_name == "xss" or bug_name == "csrf":
         return "Medium"
    else:
         return "Low"

user_bug = input("Enter vulnerability name: ").lower()

severity = evaluate_vulnerability(user_bug)
print(f"Vulnerability Impact: {severity}")



