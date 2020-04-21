# -*- coding: utf-8 -*-
#!/usr/bin/env python

from socket import *
from telnetlib import Telnet
from time import time, sleep
from sys import argv
from struct import pack, unpack
from hashlib import sha256
import itertools

def read_until(s, c):
    ret =""
    while 1:
        ret += s.recv(1)
        if ret.endswith(c):
            return ret

def p(x):
    return pack("<Q", x)

def u(x):
    return unpack("<Q", x)[0]
    

def interact(s):
    print("[*] connect")
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

def proof_of_work(plain, digest):
    target_char = [chr(x) for x in range(48, 123)]
    print(target_char)
    for i in itertools.permutations(target_char, 4):
        proof = "".join(i) + plain
        #print(proof)
        if sha256(proof).hexdigest() == digest:
            print("hit!")
            return "".join(i)


def main():
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((HOST, PORT))

    _ = read_until(s, "sha256(XXXX+")
    plain_message = read_until(s, ")").strip(")")
    _ = read_until(s, "== ")
    digest_message = read_until(s, "\n").strip("\n")

    print(plain_message)
    print(digest_message)
    
    xxxx = proof_of_work(plain_message, digest_message)

    read_until(s, "Give me XXXX:")
    s.send(xxxx)

    print(read_until(s, "\n"))


if __name__ == '__main__':
    main()