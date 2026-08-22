import numpy

if __name__ == '__main__':
    arr = numpy.array(list(map(int, input().split())))
    print(arr.reshape(3, 3))