if __name__ == '__main__':
    N, M = map(int, input().split())

    # Top Part
    for i in range(1, N, 2):
        pattern = ".|." * i
        print(pattern.center(M, "-"))

    # Middle Part
    print("WELCOME".center(M, "-"))

    # Bottom Part
    for i in range(N - 2, 0, -2):
        pattern = ".|." * i
        print(pattern.center(M, "-"))
            