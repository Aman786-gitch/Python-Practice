import numpy

if __name__ == '__main__':
    a=numpy.array(input().split(),float)
    x=float(input())
    
    def evaluate_polynomial(a, x):
        result = 0
        n = len(a)
  
        for i in range(n):
            power = n - i - 1
            result += a[i] * (x ** power)
  
        return result
    
    print(evaluate_polynomial(a, x))