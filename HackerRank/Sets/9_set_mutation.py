if __name__ == '__main__':
    n=int(input())
    A=set(map(int, input().split()))
    N=int(input())
    
    for i in range(0,N):
        command=input().split()
        S=set(map(int, input().split()))
        
        if command[0]=="intersection_update":
            A.intersection_update(S)
            
        elif command[0]=="update":
            A.update(S)
            
        elif command[0]=="symmetric_difference_update":
            A.symmetric_difference_update(S)
            
        elif command[0]=="difference_update":
            A.difference_update(S)
            
    print(sum(A))