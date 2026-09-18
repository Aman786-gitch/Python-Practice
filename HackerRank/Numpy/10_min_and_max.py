import numpy

if __name__ == '__main__':
    N,M=map(int, input().split())
    arr=numpy.array([input().split() for _ in range(M)],int)
    result=numpy.min(arr,axis=1)
    print(numpy.max(result))