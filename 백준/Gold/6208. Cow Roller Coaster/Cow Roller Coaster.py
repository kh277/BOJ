# 백준 6208

'''
DP[i][j] = 위치 i까지 부품을 설치했고 사용한 예산이 j일 때, 얻을 수 있는 최대 재미 값 
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(L, N, B, part):
    part.sort()

    DP = [[-1] * (B+1) for _ in range(L+1)]
    DP[0][0] = 0
    for curX, w, f, c in part:
        nextX = curX + w
        for curC in range(B+1):
            nextC = curC+c
            if DP[curX][curC] >= 0 and nextC <= B:
                DP[nextX][nextC] = max(DP[nextX][nextC], DP[curX][curC] + f)

    maxC = -1
    for i in range(B+1):
        if maxC < DP[L][i]:
            maxC = DP[L][i]

    return maxC


def main():
    L, N, B = map(int, input().split())
    part = []
    for _ in range(N):
        part.append(list(map(int, input().split())))

    print(solve(L, N, B, part))


main()
