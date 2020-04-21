for i in range(0xffffffff):
    H = i
    M = i
    while M > 0:
        H = ((M & 0xFF) + (H << 6) + (H << 16) - H) & 0xFFFFFFFF
        M >>= 8
        
    #H = H | 1 if M & 1 else H & 0xfffffffe
    print("[*]round{}: 0x{:x}".format(i, H))
    if H == 0x3b71ec3d or H == 0x3b71ec3c:
        print("[*]hit!... 0x{:x}".format(M))
        exit()
