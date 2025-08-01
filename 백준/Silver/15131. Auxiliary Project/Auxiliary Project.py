# 백준 15131

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N):
    if N < 5:
        return [0, 0, 1, 7, 4][N]
    
    return (N-2)//3*7 + [1, 7, 4][(N-2)%3]


def main():
    N = int(input())
    print(solve(N))


main()
