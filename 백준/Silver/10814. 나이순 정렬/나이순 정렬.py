# 백준 10814

import sys

input = sys.stdin.readline


def solve() -> list:
    data.sort(key= lambda x: (int(x[0]), x[2]))

    return [x[:2] for x in data]


# main 함수 ----------
N = int(input())

data = []
for i in range(N):
    a, b = map(str, input().split())
    data.append([a, b, i])

for i in solve():
    print(*i)