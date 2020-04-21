#!/usr/bin/python
# -*- Coding: utf-8 -*-

answer = ""

with open("result.txt", "r") as f:
    for l in f.readlines():
        answer += l[7:8]

print("[*]Flag is ...")
print(answer[:-1])
