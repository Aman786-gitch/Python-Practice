import numpy

def arrays(arr):
    new_arr=numpy.array(arr,float)
    return (new_arr[::-1])
    #numpy.flip(new_arr) can be used to reverse it
    
    

arr = input().strip().split(' ')
result = arrays(arr)
print(result)