# Uses python3
import sys


def gcd_naive(a, b):
    while b != 0:
        r = a % b
        a, b = b, r
    return a


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))
