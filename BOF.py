
import socket #Package = socket import

buff = "HELP"  

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creation of Socket
s.connect(("192.168.8.107", 9999)) #Connection
print(s.recv(1024)) #Print the response 
s.send(buff)
s.send(buff)
print(s.recv(1024))
s.close()