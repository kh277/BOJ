# 백준 1931

'''
가능한 회의의 최대 개수를 구하는 것이 목표이다.
끝나는 시간이 짧을수록, 회의의 시작하는 시간이 더 빠를 수록 더 많은 회의를 할 수 있게 된다.

주의 반례
2
0 0
0 0

3
4 4
3 4
2 4
'''

import sys
from queue import PriorityQueue

input = sys.stdin.readline


def solve(N: int, x: list) -> list:
    x.sort(key = lambda x: (x[1], x[0]))
    result = 0  # 가능한 회의의 개수
    time = 0    # 현재 시간
    for i in x:
        if time <= i[0]:
            time = i[1]
            result += 1

    return result


def main():
    N = int(input())
    x = []
    for i in range(N):
        a, b = map(int, input().split())
        x.append((a, b))

    print(solve(N, x))


main()
