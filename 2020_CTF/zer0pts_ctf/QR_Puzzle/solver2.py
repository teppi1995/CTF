import numpy as np
import re
import matplotlib.pyplot as plt

encqr_list = []
key_list = []



with open("encrypted.qr") as f:
    for line in f.readlines():
        encqr_list.append([int(x) * 255 for x in line[:-1]])

    print(encqr_list)
    
with open ("key") as f:
    for line in f.readlines():
       key_list.append([int(x) for x in re.split("[#(,)\n]",line) if x != ""])
    del key_list[-1]

    print(key_list)
        
for i, y, x in key_list:
    if i == 0:
        tmp = encqr_list[x][y]
        encqr_list[y][x] = encqr_list[y][x-1]
        encqr_list[y][x-1] = tmp
    elif i == 1:
        tmp = encqr_list[y][x]
        encqr_list[y][x] = encqr_list[y][x+1]
        encqr_list[y][x+1] = tmp
    elif i == 2:
        tmp = encqr_list[y][x]
        encqr_list[y][x] = encqr_list[y-1][x]
        encqr_list[y-1][x] = tmp
    elif i == 3:
        tmp = encqr_list[y][x]
        encqr_list[y][x] = encqr_list[y+1][x]
        encqr_list[y+1][x] = tmp

print(encqr_list)

qr_img = np.array(encqr_list, dtype = np.uint8)
plt.imshow(qr_img, cmap = 'gray', vmin = 0, vmax = 255, interpolation = 'none')
plt.show()
