from itertools import combinations

if __name__ == '__main__':
    command=input().split()
    S=sorted(command[0])
    k=int(command[1])
    
    for i in range(1,k+1):
        for j in combinations(S,i):
            print("".join(j))
            
        