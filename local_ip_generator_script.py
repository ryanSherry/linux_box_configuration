import sys, webbrowser

ip = sys.argv[1]
outbound_ip = sys.argv[2]
port = sys.argv[3]
user = sys.argv[4]
password = sys.argv[5]

usable_ips = 13
total_ips = 15
offset = 2

outbound_ip_array = outbound_ip.split(".")

	
print(f'For {ip}:')
print('')

for number in range(int(port), int(port)+usable_ips):
	print(f'{ip}:{number}:{user}:{password}')
	
print('')

print(f'For windows config file:')
for number in range(int(port), int(port)+usable_ips):
	print(f'http_port {number}')

print('')

calculated_port = int(port)
for number in range(int(outbound_ip_array[3])+offset, int(outbound_ip_array[3])+total_ips):
    print(f'acl port_{calculated_port} myportname {calculated_port} src localhost')
    print(f'http_access allow port_{calculated_port}')
    print(f'tcp_outgoing_address {outbound_ip_array[0]}.{outbound_ip_array[1]}.{outbound_ip_array[2]}.{number} port_{calculated_port}')
    calculated_port += 1
    print('')