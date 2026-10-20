#port_facts.py
#Count Ports and IPv4 Addresses

# RFC 9293 - TCP Header Port Numbers
# RFC 791 - Internet Protocol IPv4

PORT_BITS = 16
IP_BITS = 32

total_ports = 2 ** PORT_BITS
highest_port = total_ports - 1
total_ipv4 = 2 ** IP_BITS

print(f"Total possible ports: {total_ports}")
print(f"Highest port number: {highest_port}")
print(f"Total possible IPv4 addresses: {total_ipv4}")