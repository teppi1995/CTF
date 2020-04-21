from pwn import *
import re
context(os='linux', arch='amd64')
binary = asm("""
jmp 0x400bb0 
""".format(**locals()), arch='amd64')
hexstr =  re.split('(..)',binary.encode('hex_codec'))[1::2]
print(' '.join(map(str, hexstr)))
