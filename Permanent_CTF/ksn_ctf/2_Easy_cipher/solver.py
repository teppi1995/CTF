# -*- coding: utf-8 -*-

filename = "encrypted_flag"

def _rot_i(c, i):
  if 'A' <= c and c <= 'Z':
    return chr((ord(c) - ord('A') + i) % 26 + ord('A'))

  if 'a' <= c and c <= 'z':
    return chr((ord(c) - ord('a') + i) % 26 + ord('a'))

  return c
  
def main():
  with open(filename, "r") as file:
    line = file.readline()
    
    for i in range(0, 26):
      print("[*]rot " + str(i))
      dec_line = ""
      for c in line:
        dec_line += _rot_i(c, i)
        
      print(dec_line + "\n")
        
if __name__ == "__main__" :
  main()
