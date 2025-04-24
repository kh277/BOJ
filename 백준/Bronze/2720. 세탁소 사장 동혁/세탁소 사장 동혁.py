# 백준 11005

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(C):
    coin = [25, 10, 5, 1]
    count = [0, 0, 0, 0]

    for i in range(4):
        count[i] = C // coin[i]
        C = C % coin[i]
    
    return count


def main():
    T = int(input())
    for _ in range(T):
        C = int(input())
        print(*solve(C))


main()
