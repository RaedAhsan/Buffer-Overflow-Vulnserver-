from pathlib import Path
from boofuzz import*

#server
ip = "192.168.8.107"
port = 9999

connection = SocketConnection(ip, port, proto="tcp")
target = Target(connection=connection)
session = Session(target=target)

#fuzz
s_initialize("vulnserver-trun")

s_string("TRUN", fuzzable=False)
s_delim("",fuzzable=False)
s_string("something")

session.connect(s_get("vulnserver-trun"))

session.fuzz()