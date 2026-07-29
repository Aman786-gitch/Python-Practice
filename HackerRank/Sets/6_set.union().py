if __name__ == '__main__':
    n=int(input())
    E=set(map(int, input().split()))
    b=int(input())
    F=set(map(int, input().split()))
    E=E.union(F)
    print(len(E))