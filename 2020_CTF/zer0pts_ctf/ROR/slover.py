with open("chall.txt") as f:
    lines = f.readlines()

flag_bits = ""
for line in lines:
    if int(line) % 2 == 0:
        flag_bits += "0"
    else:
        flag_bits += "1"
        
flag_bits = flag_bits[::-1]

print(flag_bits)
print(int(flag_bits, 2).to_bytes(64, byteorder='big'))
