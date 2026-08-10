from itertools import groupby

if __name__ == '__main__':
    S=input()
    
    for key,group in groupby(S):
        print((len(list(group)), int(key)), end=" ")