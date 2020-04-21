import logging
from Crypto.Cipher import AES
import hashlib
import re


logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

message_digest = "356280a58d3c437a45268a0b226d8cccad7b5dd28f5d1b37abf1873cc426a8a5"
phone_id1 = "99999991"

def get_phone_ID():
    for i in range(10000000):
        ID = phone_id1 + "{:0=7}".format(i)
        print(ID)
        hash_ = hashlib.sha256(ID).hexdigest()

        if hash_ == message_digest:
            return ID

def main():
    password = str(get_phone_ID())
    print("device ID was found :" + password)
        
    
if __name__ == "__main__":
    main()
