#!/usr/bin/python
# -*- Coding: utf-8 -*-

from Crypto.Cipher import AES
from PIL import Image
from io import BytesIO
import binascii
import hashlib
import base64


half_device_id = "99999991"
hashed_device_id = "356280a58d3c437a45268a0b226d8cccad7b5dd28f5d1b37abf1873cc426a8a5"
initial_vector = "kLwC29iMc4nRMuE5"

filename = "jewel_c.png"

def find_device_id(half_id, hashed_id):
    for i in range(10000000):
        device_id = half_id + "{:07d}".format(i)
        hashed = hashlib.sha256(device_id.encode('utf-8')).hexdigest()

        if hashed == hashed_id:
            return device_id

def get_decrypt_data(cipher_data, key, iv):
    secret_key = hashlib.sha256(key.encode('utf-8')).digest()
    iv = hashlib.md5(iv.encode('utf-8')).digest()
    crypto = AES.new(secret_key, AES.MODE_CBC, iv)
    raw_data = crypto.decrypt(cipher_data)
    return raw_data
        
def main():
    print("[*]device id is ...")
    device_id = find_device_id(half_device_id, hashed_device_id)
    print(device_id)

    with open(filename, 'rb') as f:
        binary = f.read()
        ascii_hex = binascii.b2a_hex(binary)

        decrypt_data = get_decrypt_data(ascii_hex, device_id, initial_vector)
        print(decrypt_data)
        img = Image.open(BytesIO(binascii.a2b_hex(decrypt_data)))
        img.show()

        
if __name__ == "__main__":
    main()

    
