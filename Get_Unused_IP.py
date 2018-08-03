import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.connect(("www.google.com",80))

myaddr = s.getsockname()[0]

s.close()

print(myaddr)
