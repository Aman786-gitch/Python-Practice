if __name__ == '__main__':
    T=int(input())
    
    for i in range(0,T):
        a_ele=int(input())
        A=set(map(int, input().split()))
        b_ele=int(input())
        B=set(map(int, input().split()))
        
        if A.issubset(B):
            print(True)
            
        else:
            print(False)