import os
import binascii

os.system('ifconfig | grep netmask > subnet.txt') 
with open('subnet.txt') as f:
	fields = f.readlines()[-1].rstrip().split()
	print(fields[3])
	binary_string = binascii.unhexlify(fields[3])