import requests
def check_status(url):
    response = requests.get(url)
    if response.status_code == 200:
        print(f"[+] {url} is Online & Reachable! (Status Code:200)")
    else:
        print(f"[-] {url} returned Status Code: {response.status_code}")

link = input("Enter URL to check: ").lower()
check_status(link)