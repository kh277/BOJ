# 백준 28125

'''
달러와 마르크는 무조건 전부 교환하는 것이 이득이다.
DP[i][type] = i일에 가지는 달러 또는 마르크의 수
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
DOLLAR = 0
MARKS = 1


def solve(N, data):
    DP = [[0]*2 for _ in range(N+1)]
    DP[0][MARKS] = 100
    
    for i in range(1, N+1):
        MtoD = data[i][DOLLAR]/100
        DtoM = 100/data[i][MARKS]
        DP[i][DOLLAR] = max(DP[i-1][MARKS]*MtoD, DP[i-1][DOLLAR])
        DP[i][MARKS] = max(DP[i-1][DOLLAR]*DtoM, DP[i-1][MARKS])

    return round(DP[N][MARKS], 5)


def main():
    N = int(input())
    data = [None]
    for _ in range(N):
        data.append(list(map(int, input().split())))

    print(f"{solve(N, data):.2f}")


main()
