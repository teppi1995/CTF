import numpy as np
import re
import matplotlib.pyplot as plt

dec_qr_list = []

with open("dec_qr") as f:
    for line in f.readlines():
        dec_qr_list.append([int(x) * -255 + 255 for x in line[:-1]])

    print(dec_qr_list)
    
qr_img = np.array(dec_qr_list, dtype = np.uint8)
plt.imshow(qr_img, cmap = 'gray', vmin = 0, vmax = 255, interpolation = 'none')
plt.show()
