import requests
with open("URL.txt", "r") as file:
    t = file.readlines()
    for targets in t:
        domains = targets.strip()
        try:
           res = requests.get(domains)
           if res.status_code == 200:
               print(f"{domains} is online & reachable! (Status Code: {res.status_code})")
           else:
               print(f"An error occurred {domains}. (Status Code {res.status_code})")
        except Exception as e:
            print(f"An error occurred while trying to connect to server:{e}")


