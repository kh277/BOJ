# 백준 32208

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(x, y, z):
    if z % 2 == 0 and (x+y) % 2 == 0:
        return 'YES'
    elif z % 2 == 1 and (x+y) % 2 == 1:
        return 'YES'
    return 'NO'


def main():
    N = int(input())
    for _ in range(N):
        x, y, z = map(int, input().split())
    
        print(solve(x, y, z))


main()
