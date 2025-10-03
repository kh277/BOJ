# 백준 27648

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, M, K):
    if N+M-1 > K:
        return [['NO']]
    
    result = [[0 for _ in range(M)] for _ in range(N)]
    for y in range(N):
        for x in range(M):
            result[y][x] = y+x+1
    
    return [['YES']] + result


def main():
    N, M, K = map(int, input().split())
    for i in solve(N, M, K):
        print(*i)


main()
