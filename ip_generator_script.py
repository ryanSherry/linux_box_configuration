import sys

ip = sys.argv[1]
port = sys.argv[2]
user = sys.argv[3]
password = sys.argv[4]

ipArray = ip.split(".")

for number in range(int(ipArray[3])+2, int(ipArray[3])+15):
	print(f'{ipArray[0]}.{ipArray[1]}.{ipArray[2]}.{number}:{port}:{user}:{password}')