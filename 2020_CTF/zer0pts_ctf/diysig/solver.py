from fractions import Fraction
import logging
from pwn import *

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

#target Host
HOST = "18.179.178.246"
PORT = 3001
logging.info("***remote exploit ***")
logging.info("[*]target host : " + HOST)
logging.info("[*]target port : " + str(PORT))

def LSB_oracl():
    b2s = lambda ba: ''.join(list(map(chr, ba)))
    s2b = lambda st: b''.join(list(map(lambda c: bytes([ord(c)]), list(st))))
    #RSA
    N = 0x6d70b5a586fcc4135f0c590e470c8d6758ce47ce88263ff4d4cf49163457c71e944e9da2b20c2ccb0936360f12c07df7e7e80cd1f38f2c449aad8adaa5c6e3d51f15878f456ceee4f61547302960d9d6a5bdfad136ed0eb7691358d36ae93aeb300c260e512faefe5cc0f41c546b959082b4714f05339621b225608da849c30f

    E = 0x10001

    C = 0x3cfa0e6ea76e899f86f9a8b50fd6e76731ca5528d59f074491ef7a6271513b2f202f4777f48a349944746e97b9e8a4521a52c86ef20e9ea354c0261ed7d73fc4ce5002c45e7b0481bb8cbe6ce1f9ef8228351dd7daa13ccc1e3febd11e8df1a99303fd2a2f789772f64cbdb847d6544393e53eee20f3076d6cdb484094ceb5c1

    bounds = [0, Fraction(N)]
    counter = 0
    
    while True:
        counter += 1
        
        target = remote(HOST, PORT)
        _ = target.readuntil("> ")
        target.sendline("2")
        _ = target.readuntil("ENC : ")
        
        C_2 = C * pow(2, E, N) % N

        target.sendline("{:x}".format(C_2))
        _ = target.readuntil("SIG : ")
        target.sendline("00")
        _ = target.readuntil("Invalid Signature: 00000000 != ")
        signature = int.from_bytes(bytes.fromhex(b2s(target.readline()[:-1])), byteorder='big')

        if signature % 2 == 1:
            bounds[0] = sum(bounds) / 2
        else:
            bounds[1] = sum(bounds) / 2

        diff = bounds[1] - bounds[0]
        diff = diff.numerator / diff.denominator

        if diff == 0:
            m = bounds[1].numerator // bounds[1].denominator
            return m
        
        C = C_2
        logging.info("[*]round{} ...Done".format(counter))
        logging.info("{}/{} ~ {}/{}".format(bounds[0].numerator, bounds[0].denominator, bounds[1].numerator, bounds[1].denominator))
        logging.info("######################################################\n")
        target.close()
        

        
def main():
    M = LSB_oracl() 
    print(M.to_bytes(64, byteorder="big"))
    
if __name__ == "__main__":
    main()
