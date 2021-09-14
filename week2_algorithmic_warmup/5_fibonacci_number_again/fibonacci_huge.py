# Uses python3
import sys


def get_fibonacci_huge_naive(n, m):
    fib = [0, 1]
    r = [0, 1]
    flag = False
    if n >= 2:
        for i in range(2, n + 1):
            fib.append(fib[i - 1] + fib[i - 2])
            r.append(fib[i] % m)
            if (r[-1] == 1) and (r[-2] == 0):
                flag = True
                r = r[:-2]
                break
    if flag:
        return r[n % len(r)]
    else:
        return fib[n] % m


if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
