import string

def print_rangoli(size):
    alpha = string.ascii_lowercase
    width = 4 * size - 3

    # Top half (smallest to middle)
    for i in range(size - 1, -1, -1):
        s = "-".join(alpha[size-1:i:-1] + alpha[i:size])
        print(s.center(width, "-"))

    # Bottom half
    for i in range(1, size):
        s = "-".join(alpha[size-1:i:-1] + alpha[i:size])
        print(s.center(width, "-"))

if __name__ == "__main__":
    n = int(input())
    print_rangoli(n)