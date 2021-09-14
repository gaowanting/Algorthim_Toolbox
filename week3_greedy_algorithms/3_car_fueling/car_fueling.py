# python3
import sys

# tank means the largest safe move


def compute_min_refills(distance, tank, stops):
    current_position = 0
    next_position = 0
    refills_num = 0
    while stops[current_position] < distance:
        while stops[next_position] < distance:
            if stops[next_position+1] - stops[current_position] < tank:
                next_position += 1
        if current_position == next_position:
            return -1
        else:
            current_position = next_position
            refills_num += 1
    return refills_num


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
