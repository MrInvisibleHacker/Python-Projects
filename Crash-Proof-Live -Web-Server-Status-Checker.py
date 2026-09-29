import requests
def live_website():
    try:
        link = input("Enter website link: ")
        response = requests.get(link)
        if response.status_code == 200:
           print(f"[+] {link} is online and reachable. Status Code:{response.status_code}")
        else:
            print(f"[-] {link} returned Status Code: {response.status_code}")
    except Exception as e:
        print(f"[!]An Error Occurred: {e}")

live_website()
