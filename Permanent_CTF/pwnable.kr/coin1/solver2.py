#!/usr/bin/python
# -*- coding:utf-8 -*-
import socket, struct, telnetlib

# --- common funcs ---
def sock(remoteip, remoteport):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((remoteip, remoteport))
    return s

def read_until(s, delim='\n'):
    data = ''
    while not data.endswith(delim):
        chr = str(s.recv(1))
        data += chr
    return data

def shell(s):
    t = telnetlib.Telnet()
    t.sock = s
    t.interact()

def p(a): return struct.pack("<I",a)
def u(a): return struct.unpack("<I",a)[0]


# --- target info ---

target_host = "pwnable.kr"
target_port = 9007


if __name__ == "__main__":
    s = sock(target_host, target_port)
    #_ = read_until(s, "starting in 3")
    _ = read_until(s, "- Ready? starting in 3 sec... -")
    _ = read_until(s, "\n\t\n")
    
    for i in range(100):
        #_ = read_until(s, "N=")
        right = int(s.recv(15).strip("N=").split(" C=")[0])
        #right = int(l[0])
        #C = int(l[1])
        #print("N = " + str(N))
        #print("C = " + str(C))

        left = 1
        #right = N
        
        while(1):
            inter = int((left + right + 1) / 2)
            request = " ".join([str(x) for x in range(left, inter)]) + "\n"
            s.sendall(request)
            response = s.recv(15).strip()

            if response.startswith("Corr"):
                print(response)
                break
            elif response.startswith("Wrong"):
                print(response)
                exit(1)
            elif response.startswith("format"):
                print(request)
                print(response)
                exit(1)
            
            else:
                answer = int(response)
                if answer == 10:
                    left += 1
                    inter += 1
                    continue
                elif answer == 9:
                    continue
                elif answer % 10 != 0:
                    right = inter
                    continue
                else:
                    left = inter
                    continue
                
    flag = s.recv(100).strip()
    print(flag)
