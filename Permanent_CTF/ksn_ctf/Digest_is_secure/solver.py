import requests
import hashlib
from bs4 import BeautifulSoup as bs

url = "http://ksnctf.sweetduet.info:10080/~q9/flag.html"


md5a1 = "c627e19450db746b739f41b64097d449"
nonce = ""
nc = "00000001"
cnonce = "5f70c9b7a0f15b7d"
qop = "auth"
a2 = "GET:/~q9/flag.html"
md5a2 = "ffffdd8b8029499600f95a69beb239c2"

username = "q9"
realm = "secret"
algorithm = "MD5"
uri = "/~q9/flag.html"

def get_md5(arg):
    return hashlib.md5(arg.encode('utf-8')).hexdigest()

def main():
    auth_header = requests.get(url).headers["WWW-Authenticate"]
    print(auth_header)

    nonce = auth_header.split(" ")[2][7:-2]

    response = md5a1 + ":" + nonce + ":" + nc + ":" + cnonce + ":" + qop + ":" +  md5a2
    md5_response = get_md5(response)

    headers = {
        "Authorization": \
        "Digest username=\"" + username + "\"" + \
        ", realm=\"" + realm + "\"" + \
        ", nonce=\"" + nonce + "\"" + \
        ", uri=\"" + uri + "\"" + \
        ", algorithm=\"" + algorithm + "\"" + \
        ", response=\"" + md5_response + "\"" + \
        ", qop=" + qop + \
        ", nc=" + nc + \
        ", cnonce=\"" + cnonce + "\""
    }

    answer = requests.get(url, headers=headers)

    answer_soup = bs(answer.text, "html.parser")
    print(answer_soup.p.text)

    
if __name__ == "__main__":
    main()
