from itertools import combinations

if __name__ == '__main__':
    N=int(input())
    l=input().split()
    K=int(input())
    
    result=list(combinations(l,K))
    total=len(result)
    count=0

    for i in result:
        if "a" in i:
            count += 1
            
    print(count/total)