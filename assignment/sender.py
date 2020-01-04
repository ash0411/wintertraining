import socket
from cryptography.fernet import Fernet
target_ip = "127.0.0.1"
target_port = 1235
# now we are creating udp socket -- this is for all sender and reciever
# it means we use ipv4,UDP
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#this is only for reciever
# s.bind((target_ip,target_port))

while True:
#this is for sender
	msg = input("please enter your message : ")
	cipher_key=b'GzDqzcu4kz52ZOyu7haSaWY4t4mE2jzSKD4JuYfm7VE='
	#cipher_key = Fernet.generate_key()
	#print(cipher_key)
	cipher = Fernet(cipher_key)
	message = msg.encode()
	encrypted = cipher.encrypt(message)
	#new_msg = msg.encode('ascii')
	#message = b'the quick brown fox jumps over the lazy dog'
	#encrypted_message = cipher.encrypt(message)
	out_message=encrypted.decode()# turn it into a string to send
	new_msg = out_message.encode('ascii')
	#print(new_msg)
	# we have to encode string to byte like object in python3 only
	s.sendto(new_msg,(target_ip,target_port))
	print(s.recvfrom(100))
 
