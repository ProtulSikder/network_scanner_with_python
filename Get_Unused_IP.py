import ipaddress,netifaces,subprocess,socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.connect(("www.google.com",80))

my_ip = s.getsockname()[0]

for i in netifaces.interfaces():
	if netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'] == my_ip:
		my_subnet = netifaces.ifaddresses(i)[netifaces.AF_INET][0]['netmask']
		iface = i

cidr = sum([bin(int(i)).count("1") for i in my_subnet.split('.')])

full_ip = my_ip + "/" + str(cidr)

my_network = ipaddress.ip_interface(full_ip).network

for ip in my_network.hosts():
	r = subprocess.call(['ping','-q','-c','1',str(ip)], stdout = subprocess.DEVNULL)

	if r == 0:
		print("{} is active".format(str(ip)))
	else:
		print("{} is not active".format(str(ip)))
