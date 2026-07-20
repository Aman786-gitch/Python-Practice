def sy_difference(M,a,N,b):
    c=a.symmetric_difference(b)
    c=sorted(c)
    for n in c:
        print(n)
    
if __name__ == '__main__':
    M=int(input())
    a=set(map(int,input().split()))
    N=int(input())
    b=set(map(int,input().split()))
    sy_difference(M,a,N,b)
    