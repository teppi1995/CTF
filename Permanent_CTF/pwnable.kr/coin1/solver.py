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

def search_counterfeit_coin(s, left, right):

    inter = int((left + right + 1) / 2)
    #print ("left = " + str(left) + " right = " + str(right) + " inter = " + str(inter))
    
    request = " ".join([str(x) for x in range(left, inter)]) + "\n"
    s.sendall(request)
    answer = int(s.recv(5).strip())
    #print(answer)
    
    if answer == 10:
        return inter
    elif answer == 9:
        return left
    elif answer % 10 != 0:
        return search_counterfeit_coin(s, left, inter)
    else:
        return search_counterfeit_coin(s, inter , right)
        


if __name__ == "__main__":
    s = sock(target_host, target_port)
    #_ = read_until(s, "starting in 3")
    _ = read_until(s, "N=")

    for i in range(100):
        _ = read_until(s, "N=")
        N = int(read_until(s, "C=").strip(" C="))
        C = int(s.recv(3).strip())
        #print("N = " + str(N))
        #print("C = " + str(C))

        counterfeit_coin = str(search_counterfeit_coin(s, 1, N)) + "\n"

        while(1):
            s.sendall(counterfeit_coin)
            response = s.recv(30).strip()
            print(response)
            if response.startswith("Correct!"):
                break
            elif response.startswith("Wrong"):
                exit(1)
        

    flag = s.recv(30).strip()
    print(flag)
