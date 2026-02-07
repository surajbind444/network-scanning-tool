import nmap

scanner = nmap.PortScanner()
target = input("Enter target IP: ")

scanner.scan(target, '1-1024', '-sT')

for host in scanner.all_hosts():
    print(f"\nHost: {host}")
    for proto in scanner[host].all_protocols():
        print(f"Protocol: {proto}")
        for port in scanner[host][proto]:
            state = scanner[host][proto][port]['state']
            service = scanner[host][proto][port]['name']
            print(f"Port {port} | {state} | {service}")
