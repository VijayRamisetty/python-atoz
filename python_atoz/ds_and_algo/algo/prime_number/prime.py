import math


def is_prime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            print(f"{x} is Not Prime")
            break
    else:
        print(f"{x} is Prime")


if __name__ == '__main__':
    n = 100
    for x in range(1, n):
        is_prime(x)
