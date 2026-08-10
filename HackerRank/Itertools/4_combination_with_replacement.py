from itertools import combinations_with_replacement

if __name__ == '__main__':
    command=input().split()
    S=sorted(command[0])
    k=int(command[1])
    
    for i in combinations_with_replacement(S,k):
        print("".join(i))