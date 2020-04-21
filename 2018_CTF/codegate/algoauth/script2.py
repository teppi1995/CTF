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

def calc_route(array):
    answer = 82
    return str(answer) + '\n'
    
def main():
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((HOST, PORT))

    print("[*] connetc to remote")

    _ = read_until(s, "you want to start, type the G key within 10 seconds....>>")
    s.sendall("G\n")

    quiz_count = 1
    
    while (1):
        print("number " + str(quiz_count))
        _ = read_until(s, "***")
        _ = read_until(s, "***\n")
        array= read_until(s, "Answer within")
        #print array
        
        arr = []
        arr2 = []
        count = 0
        
        for line in array.split('\n'):
            for num in line.split():
                #print num
                arr.append(int(num))
            count += 1
            if count > 7:
                break
            arr2.append(arr)
            arr = []
                
        print arr2
                
        s.sendall(calc_route(arr2))
        quiz_count += 1
    
if __name__ == "__main__":
    main()
    
        

