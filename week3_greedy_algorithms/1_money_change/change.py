# Uses python3
import sys


def get_change(m):
    num_10 = m // 10
    m = m % 10
    num_5 = m // 5
    m = m % 5
    num_1 = m
    total_num = num_10 + num_5 + num_1
    return total_num


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
