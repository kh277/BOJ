# 백준 29018

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve():
    string = sorted(N)

    small = ""
    large = ""
    num = ""

    for i in string:
        cur = ord(i)
        if ord('a') <= cur <= ord('z'):
            small += i
        elif ord('A') <= cur <= ord('Z'):
            large += i
        elif ord('0') <= cur <= ord('9'):
            num += i

    return small + large + num


# main 함수 ----------
while True:
    N = input().decode().rstrip()
    if N == "#":
        break
    print(solve())
