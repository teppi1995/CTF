import random
import signal
import time
import gmpy2
from Crypto.Util.number import inverse, bytes_to_long, long_to_bytes


def s2n(s):
    return bytes_to_long(bytearray(s, 'latin-1'))


def n2s(n):
    return long_to_bytes(n).decode('latin-1')

def main():
    
    print(s2n("1"))

if __name__ == "__main__":
    main()


