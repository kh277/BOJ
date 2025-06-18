# 백준 4307

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, L, ant):
    ant.sort()

    # 구간 [0, N/2]의 개미는 왼쪽, 구간 [N/2, N]의 개미는 오른쪽으로 보도록 하기
    minT = 0
    maxT = 0
    for i in range(N):
        if ant[i] < L/2:
            minT = max(minT, ant[i])
            maxT = max(maxT, L-ant[i])
        else:
            minT = max(minT, L-ant[i])
            maxT = max(maxT, ant[i])
    
    return [minT, maxT]


def main():
    T = int(input())
    for _ in range(T):
        L, N = map(int, input().split())
        ant = []
        for _ in range(N):
            ant.append(int(input()))
        print(*solve(N, L, ant))


main()
