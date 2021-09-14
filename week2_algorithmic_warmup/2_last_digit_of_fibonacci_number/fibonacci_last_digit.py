# Uses python3
import sys


def get_fibonacci_last_digit_naive(n):
    fib = [0, 1]
    if n >= 2:
        for i in range(2, n + 1):
            fib.append(fib[i - 1] + fib[i - 2])
    result = fib[n] % 10
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))

