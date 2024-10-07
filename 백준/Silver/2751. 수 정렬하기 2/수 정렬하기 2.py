# 백준 2751


import sys

input = sys.stdin.readline


def solve() -> int:
    return sorted(num)


# main 함수 ----------
N = int(input())

num = []
for _ in range(N):
    num.append(int(input()))

for i in solve():
    print(i)
