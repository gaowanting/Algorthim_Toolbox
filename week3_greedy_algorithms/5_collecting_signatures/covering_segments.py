# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def end(i):
    return i.end


def optimal_points(segments):
    segments.sort(key=end)
    points = []
    while len(segments) != 0:
        i = 0
        points.append(segments[i].end)
        while len(segments) > 1:
            if segments[i + 1].start <= segments[i].end:
                segments.pop(1)
            else:
                break
        segments.pop(0)
        # elif len(segments) == 1:
    return points


if __name__ == '__main__':
    input = sys.stdin.read()
    # input = '4 4 7 1 3 2 5 5 6'
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
