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

reslist = []
inlist = []

def calcnum(x,y,num):
    #print("x="+str(x)+",y="+str(y))
    resnum = num + inlist[x][y]
    print reslist[x][y]
    if reslist[x][y] > resnum:#比較
        reslist[x][y] = resnum
		
	if y<6:
	    if x>0:calcnum(x-1,y,resnum)
            else:return
			
	    calcnum(x,y+1,resnum)
			
	    if x<6:calcnum(x+1,y,resnum)
	    else:return
			
	else:
	    return 

        
def calc_route():
    reslist = [[999 for i in range(7)] for j in range(7)]
    print reslist
    minnum = 999	
    for n in range(7):
	calcnum(n,0,0)

    print reslist
    
    for n in range(7):
	if minnum > reslist[n][6]:
            print minnum
	    minnum = reslist[n][6]

    print "answer : " + str(minnum)
    return str(minnum) + '\n'


def main():
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((HOST, PORT))

    print("[*] connetc to remote")

    _ = read_until(s, "you want to start, type the G key within 10 seconds....>>")
    s.sendall("G\n")

    quiz_count = 1
    
    while (1):
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
            inlist.append(arr)
            arr = []
                
        print inlist
                
        s.sendall(calc_route())
        quiz_count += 1
    
if __name__ == "__main__":
    main()
    
        

