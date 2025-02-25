import logging
import math

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

PI2 = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091

def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True

                   
def main():
    PI_str = str(PI2).replace(".", "")
    
    for i in range(len(PI_str) - 10):
        if is_prime(int(str(PI_str[i:i + 10]))):
            print("FLAG_Q20_{" + PI_str[i:i + 10] + "}")
            exit()
            
    print("Failed")
    
    
if __name__ == "__main__":
    main()
