# -*- coding: utf-8 -*-
#!/usr/bin/env python

from socket import *
from telnetlib import Telnet
from time import time, sleep
from sys import argv
from struct import pack, unpack

def read_until(s, c):
    ret = ""
    while 1:
        ret += s.recv(1)
        if ret.endswith(c):
            return ret        
        
def p(x):
    return pack("<Q", x)

def u(x):
    return unpack("<Q", x)[0]

def interact(s):
    print("[*] connect to remote")
    t = Telnet()
    t.sock = s
    t.interact()

if len(argv) >= 2 and argv[1] == "r":
    print("[*] connetc to remote")
    HOST = argv[2]
    PORT = int(argv[3])

else:
    print("[*] connect to local")
    HOST = "localhost"
    PORT = 9999

def main():
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((HOST, PORT))

    _ = read_until(s, "***")
    _ = read_until(s, "***")
    array= read_until(s, "Answer within")
    print array

    
if __name__ == "__main__":
    main()
    
        

