# 백준 1612

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N):
    if N % 2 == 0 or N % 5 == 0:
        return -1

    count = 1
    curNum = 1
    while True:
        if curNum % N == 0:
            return count
        curNum = (curNum % N)*10 + 1
        count += 1


def main():
    N = int(input())

    print(solve(N))


main()
