def fibo(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibo(n - 2) + fibo(n - 1)


if __name__ == '__main__':
    n = 20
    for x in range(0, n):
        print(fibo(x), end=' ')
