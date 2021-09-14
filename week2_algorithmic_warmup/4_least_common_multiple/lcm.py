# Uses python3
import sys


def lcm_naive(a, b):
    c = a*b
    while b != 0:
        r = a % b
        a, b = b, r
    return int(c/a)


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))

