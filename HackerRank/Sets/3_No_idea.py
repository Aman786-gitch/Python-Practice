def happiness(arr,A,B):
    happ_count=0
    for i in arr:
        if i in A:
            happ_count += 1
            
        elif i in B:
            happ_count += -1
            
    return happ_count



if __name__ == '__main__':
    n,m=map(int, input().split())
    arr = list(map(int, input().split()))
    A=set(map(int, input().split()))
    B=set(map(int, input().split()))
    result=happiness(arr,A,B)
    print(result)