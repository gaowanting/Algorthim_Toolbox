# Uses python3
import sys


def density(i):
    return i[1]/i[0]


def get_optimal_value(capacity, weights, values):

    para_list = list(zip(weights, values))
    para_list.sort(reverse=True, key=density)
    current_capacity = capacity
    value = 0.
    i = 0
    while current_capacity > 0:
        if current_capacity >= para_list[i][0]:
            value += para_list[i][1]
            current_capacity = current_capacity - para_list[i][0]
        else:
            value += (current_capacity / para_list[i][0]) * para_list[i][1]
            current_capacity = 0
        i += 1
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
