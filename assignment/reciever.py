target_ip = "127.0.0.1"
target_port = 1235
from cryptography.fernet import Fernet
# now we are creating udp socket -- this is for all sender and reciever
# it means we use ipv4,UDP
import socket,time,pyttsx3,subprocess
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#this is only for reciever
s.bind((target_ip,target_port))
while True:
   # time.sleep(1)
	client_data = s.recvfrom(1000)
	print(client_data)
	client_datas = client_data[0].decode('ascii')
	client_datab = client_datas.encode() 
	print(type(client_datab))
	cipher_key =b'GzDqzcu4kz52ZOyu7haSaWY4t4mE2jzSKD4JuYfm7VE='
	cipher = Fernet(cipher_key)
	decrypted_message = cipher.decrypt(client_datab)   #decrypted_message = cipher.decrypt(encrypted_message)
	print("\nreceived message =",str(decrypted_message.decode("ascii")))
	audio1 = pyttsx3.init()
	audio1.say(decrypted_message)
	audio1.runAndWait()
	print(client_data)
	print("now replying  to ",client_data[1][0])
	s.sendto("hii guys thanks for the message ".encode('ascii'),client_data[1])
	subprocess.getoutput("touch " + client_data[1][0] + ".txt")
	with open(client_data[1][0]+".txt","a") as f:
		f.write(client_data[0].decode('ascii'))
		f.write("\n")
