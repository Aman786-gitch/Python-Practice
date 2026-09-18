import numpy

if __name__ == '__main__':
    N=int(input())
    a = numpy.array([
        list(map(float, input().split())) 
        for _ in range(N)
        ])
    
    print(round(numpy.linalg.det(a), 2))
   