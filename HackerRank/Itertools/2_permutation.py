from itertools import permutations

if __name__ == '__main__':
    command=input().split()
    S=sorted(command[0])
    k=int(command[1])
    
    for i in permutations(S,k):
        print("".join(i))
        