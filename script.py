role = input("Enter your role:")
password = int(input("Enter your password:"))

if role == "admin" and password == 7788:
    print("Access Granted: Full Control Unlocked!")
elif role == "tester" and password == 7788:
    print("Access Granted: Limited Testing Mode")
else:
    print("Access Denied: Invalid Credentials!")

