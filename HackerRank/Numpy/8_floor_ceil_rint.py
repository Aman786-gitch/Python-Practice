import numpy
numpy.set_printoptions(legacy='1.13')


if __name__ == '__main__':
    A=numpy.array(input().split(),float)
    print(numpy.floor(A))
    print(numpy.ceil(A))
    print(numpy.rint(A))