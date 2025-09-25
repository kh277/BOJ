# 백준 2417

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N):
    start = 0
    end = N

    while start < end:
        mid = (start+end)//2
        if mid*mid < N:
            start = mid+1
        else:
            end = mid

    return start


def main():
    N = int(input())
    print(solve(N))


main()
