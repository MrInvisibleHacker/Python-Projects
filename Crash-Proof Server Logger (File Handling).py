import  requests
website_link = input("Enter website URL to scan: ")
log_msg = f"[+]{website_link} is Online & Reachable! (Status Code: 200)\n"
try:
    response = requests.get(website_link)
    if response.status_code == 200:
        print(log_msg)
        with open("index.txt", "a") as file:
            file.write(log_msg)
    else:
        print(f"[-]{website_link} returned status code : {response.status_code}")
        with open("index.txt", "a") as file:
            file.write(f"[-]{website_link} returned status code : {response.status_code}\n")

except Exception as e:
    print(f"[!] Connection Error: {e}")
    with open("index.txt", "a") as file:
        file.write(f"\n[!]{website_link} Connection Error: {e}")

print("Result successfully saved to index.txt!")
