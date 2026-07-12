if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    winner=-100
    runner_up=-100
    
    winner=max(arr)        

    for i in arr:
        if (runner_up<i and i != winner):
            runner_up=i
            
    print(runner_up)