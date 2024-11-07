# 백준 5089

import sys

input = sys.stdin.readline


def solve(city):
    return len(city)


# main 함수 ----------
index = 1
while True:
    N = (int(input()))
    if N == 0:
        break
    city = set()
    for _ in range(N):
        city.add(input().rstrip())
    print("Week {a} {b}".format(a=index, b=solve(city)))
    index += 1