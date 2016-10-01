import os

dirpath = os.path.dirname(os.path.realpath(__file__))
subnet = '10.142'

with open(dirpath + '/good_ips.txt', 'a') as file:
	for p3 in range(256):
		for p4 in range(256):
			ip_address = subnet + '.' + str(p3) + '.' + str(p4)
			# if not os.system('ping -c 1 -W 1 ' + ip_address):
			file.write(ip_address + '\n')