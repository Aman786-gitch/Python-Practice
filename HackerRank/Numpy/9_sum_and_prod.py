import numpy

if __name__ == '__main__':
    N,M=map(int, input().split())
    arr=numpy.array([input().split() for _ in range(M)],int)
    result=numpy.sum(arr, axis = 0)
    print(numpy.prod(result))