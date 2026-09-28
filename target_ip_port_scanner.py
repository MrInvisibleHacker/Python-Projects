ip_list = ["192.168.1.1", "10.0.0.1", "172.16.0.1"]
for ip in ip_list:
     print(f"Checking IP: {ip}")

print("")

port = 80

while port<=83:
    print(f"Testing port: {port} ... Open")
    port = port + 1