

def create_array():
    arr = []
    
    f = open('text')
    lines = f.readlines() 
    f.close()

    lines_n = 0
    for line in lines:
        for num in line.split():
            arr.append(int(num))
        array.append(arr)
        arr = []

    return array

def compare(i, j, array):
    if i > 0 and i < 6:
        min = array[i + 1][j]
        if min > array[i + 1][j + 1]:
            min = array[i + 1][j + 1]
        if 
    

def aiueo(array):
    route = []
    
    for i in range(0, 7):
        for j in range(0, 7):
            compare(i, j, array)
            #print array[i][0]
        
            
            
if __name__ == '__main__':
    array = create_array()
    print array
    aiueo(array)
