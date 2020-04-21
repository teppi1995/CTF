import sys
import logging
from pwn import *
import gmpy2
from Crypto.Util.number import inverse, bytes_to_long, long_to_bytes

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)


def s2n(s):
    return bytes_to_long(bytearray(s, 'latin-1'))


def n2s(n):
    return long_to_bytes(n).decode('latin-1')


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

e = 0x10001
gomi = bytes(
    '====================================\n'
    '            fault box\n'
    '====================================\n'
    '1. print encrypted flag\n'
    '2. print encrypted fake flag\n'
    '3. print encrypted fake flag (TEST)\n'
    '4. encrypt\n'
    '====================================\n')

    
def main():
    logging.info("main!!")
    
    _ = target.recvuntil(gomi)

    ### N
    target.sendline("4")
    _ = target.recvuntil("input the data:")
    target.sendline("a")
    aN = s2n("a") ** e - int(target.recvline(), 16)
    target.sendline("4")
    _ = target.recvuntil("input the data:")
    target.sendline("b")
    bN = s2n("b") ** e - int(target.recvline(), 16)

    N = gmpy2.gcd(aN, bN)
    logging.info("modulus N = " + hex(N))
    

    ### q
    _ = target.recvuntil(gomi)
    target.sendline("2")
    encrypted_fake_flag = int(target.recvline(), 16)
    y = 0
    fake_flag = ""
    for i in range(600):
        logging.info("[*] i = " + str(i))
        fake_flag = 'fake_flag{%s}' % (('%X' % i).rjust(32, '0'))
        _ = target.recvuntil(gomi)
        target.sendline("4")
        _ = target.recvuntil("input the data:")
        target.sendline(fake_flag)
        return_e_fake_flag = target.recvline()
        logging.info(return_e_fake_flag)
        if encrypted_fake_flag == int(return_e_fake_flag, 16):
            logging.info("[*] y = " + str(i))
            y = i
            print(fake_flag)
            break

    
    _ = target.recvuntil(gomi)
    target.sendline("3")
    fake_flag_CRT = int(target.recvline(), 16)
    _ = target.recvuntil(gomi)
    target.sendline("4")
    _ = target.recvuntil("input the data:")
    target.sendline(fake_flag_CRT)
    encrypted_fS = int(target.recvline(), 16)
    q = gmpy2((s2n(fake_flag) % N - encrypted_fS), N)
        
    logging.info("q = " + hex(q))
    logging.info("p = " + hex(N / q))
    logging.info(gmpy2.is_prime(q))
    
if __name__ == "__main__":
    main()
