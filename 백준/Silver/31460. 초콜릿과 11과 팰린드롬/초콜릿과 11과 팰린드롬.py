# 백준 31460

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N):
    result = [0, 0, 11, 121]
    if N < 4:
        return result[N]
    return ''.join(['11', '0'*(N-4), '11'])


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(solve(N))


main()
