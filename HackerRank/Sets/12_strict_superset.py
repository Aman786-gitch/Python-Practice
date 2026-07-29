if __name__ == '__main__':
    A=set(map(int, input().split()))
    n=int(input())
    
    result=True
    for _ in range(0,n):
        B=set(map(int, input().split()))
        
        if not(A>B):
            result=False
            break
            
    print(result)
        
    
            