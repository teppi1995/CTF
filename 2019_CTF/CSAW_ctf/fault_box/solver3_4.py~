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

def encrypt(m, e, N):
        return pow(m, e, N)

def decrypt(c, d, N):
        return pow(c, d, N)

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
    target.sendline("3")
    fake_flag_CRT = target.recvline()

    _ = target.recvuntil(gomi)
    target.sendline("4")
    _ = target.recvuntil("input the data:")
    target.sendline(fake_flag_CRT)
    fake_flag_CRT_pow = int(target.recvline(), 16)
    
    _ = target.recvuntil(gomi)
    target.sendline("4")
    _ = target.recvuntil("input the data:")
    target.sendline("TEST")
    test = int(target.recvline(), 16)

    logging.info("fake_flag_CRT_pow = " + hex(fake_flag_CRT_pow))

    
    for i in range(1000):
        logging.info("[*] i = " + str(i))
        fake_flag = 'fake_flag{%s}' % (('%X' % i).rjust(32, '0'))
        logging.info(fake_flag)
        #logging.info((s2n(fake_flag) % N - fake_flag_CRT_pow) % N)
        q = gmpy2.gcd((s2n(fake_flag) - fake_flag_CRT_pow), N)
        p = N / q
        phi = (p-1) * (q-1)
        d = inverse(e, phi)
        if q == 0x01:
            logging.info("q = 0x01 continue")
            continue
        
        logging.info("q = " + hex(q))
        logging.info("p = " + hex(p))
        logging.info("d = " + hex(d))

        dec_test = n2s(decrypt(test, d, N))
        logging.info("decrypt_test = " + dec_test)
        if dec_test == "TEST":
            _ = target.recvuntil(gomi)
            target.sendline("1")
            encrypted_flag = int(target.recvline(), 16)    
            decrypted_flag = n2s(decrypt(encrypted_flag, d, N))

            print(decrypted_flag)
            break

        
if __name__ == "__main__":
    main()
