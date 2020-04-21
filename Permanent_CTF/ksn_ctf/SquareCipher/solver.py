import logging
import numpy as np
import matplotlib.pyplot as plt


logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

def main():
    arr = np.empty((0, 31), dtype = np.uint8)
    
    with open("cipher") as f:
        lines = f.readlines()
        for line in lines:
            arr_temp = [[]]
            for char in line:
                if char.isupper():
                    arr_temp[0].append(0)
                elif char.islower():
                    arr_temp[0].append(255)

            print(arr_temp)
            print(len(arr_temp[0]))
            arr = np.append(arr, np.array(arr_temp), axis=0)

    logging.info(arr)

    plt.imshow(arr, cmap = 'gray', vmin = 0, vmax = 255, interpolation = 'none')
    plt.show()

    

            
    
if __name__ == "__main__":
    main()
