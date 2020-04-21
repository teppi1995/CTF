import struct
import random

def p(a):
    return struct.pack("<I", a)

def u(a):
    return struct.unpack("<I", a)[0]

def enc_xor(a, b):
    return ''.join([chr(ord(c1) ^ ord(c2)) for (c1, c2) in zip(a, b)])


def unBitshiftRightXor(x, shift):
    i = 1
    y = x
    while i * shift < 32:
        z = y >> shift
        y = x ^ z
        i += 1
    return y

def unBitshiftLeftXor(x, shift, mask):
    i = 1
    y = x
    while i * shift < 32:
        z = y << shift
        y = x ^ (z & mask)
        i += 1
    return y

def untemper(x):
    x = unBitshiftRightXor(x, 18)
    x = unBitshiftLeftXor(x, 15, 0xefc60000)
    x = unBitshiftLeftXor(x, 7, 0x9d2c5680)
    x = unBitshiftRightXor(x, 11)
    return x


def main():
    f1 = open("encrypt.cpp", "r").read()  
    f2 = open("encrypt.enc", "r").read()[4:]  
    f3 = open("flag.enc", "r").read()[4:]  
  
    print("[+] len(f1)=" + str(len(f1)) + "block=" + str(len(f1)/4))
    print("[+] len(f2)=" + str(len(f2)) + "block=" + str(len(f2)/4))
    print("[+] len(f3)=" + str(len(f3)) + "block=" + str(len(f3)/4))

    
    values1 = enc_xor(f1, f2)
    encrypt_keys = []

    for i in range(len(values1) // 4):
        #print(values1[i * 4:(i + 1) * 4])
        n = u(values1[i * 4:(i + 1) * 4])
        encrypt_keys.append(n)
        
    mt_state = tuple([untemper(x) for x in encrypt_keys[:624]] + [624])
    random.setstate((3, mt_state, None))

    print("[*]Garbage...")
    for i in range(len(values1) / 4 - 624):
        garbage = random.getrandbits(32)
        print(garbage)

    flag_key = ""
    for i in range(len(f3) // 4):
        flag_key += p(random.getrandbits(32))

    recover = enc_xor(f3, flag_key)

    with open("flag.jpg","wb") as f:  
        f.write(recover)  

    print("[+] recovering finish!")  

    
if __name__ == "__main__":
    main()


