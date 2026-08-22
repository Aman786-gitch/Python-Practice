import numpy


if __name__ == '__main__':
    shape=tuple(map(int, input().split()))
    
    print(numpy.zeros(shape,dtype=int))
    
    print(numpy.ones(shape,dtype=int))