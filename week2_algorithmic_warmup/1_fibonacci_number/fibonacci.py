# Uses python3
def calc_fib(n):
    fib = [0, 1]
    if n >= 2:
        for i in range(2, n+1):
            # print(i)
            # print(fib[n - 1])
            fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]


n = int(input())
print(calc_fib(n))
