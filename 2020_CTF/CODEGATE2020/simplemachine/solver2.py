import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

def calc_flag_1(key_list):
    flag_1 = ""
    for key in key_list:
        ans = 0x10000 - key
        flag_1 += chr(ans & 0xff)
        flag_1 += chr(ans >> 8)

    return flag_1
        
def calc_flag_2(key_list, seed = 0xdead):
    flag_2 = ""
    for key in key_list:
        xor_num = ((seed * 2) ^ seed) & 0xffff
        ans = ((0x10000 - key) ^ xor_num) & 0xffff

        flag_2 += chr(ans & 0xff)
        flag_2 += chr(ans >> 8)
        
        seed = xor_num

    return flag_2

        
def main():
    key_list1 = [0xb0bd, 0xbabc, 0xbeb9, 0xbaac, 0xcfce, 0xcfce]
    key_list2 = [0xf974, 0x2b9d, 0x4caf, 0xbee1, 0xfc0d, 0x6e48, 0xe03c, 0xd322, 0x1979, 0x36d6, 0x40e8, 0xcbf7]

    print(calc_flag_1(key_list1))
    print(calc_flag_2(key_list2))
    
if __name__ == "__main__":
    main()
