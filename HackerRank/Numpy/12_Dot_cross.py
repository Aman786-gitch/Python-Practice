import numpy

if __name__ == '__main__':
    N=int(input())
    A=numpy.array([input().split() for _ in range(N)],int)
    B=numpy.array([input().split() for _ in range(N)],int)
    print(A @ B)