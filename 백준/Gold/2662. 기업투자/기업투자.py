# 백준 2662

'''
배낭 문제 + 역추적
DP[i][j] = i번째 기업까지 투자해서 사용한 금액이 j원일 때 얻는 최대 이익
'''

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, M, data):
    DP = array('I', [0]) * (N+1)
    traceback = [[] for _ in range(N+1)]

    # 베낭 DP 계산
    for curCorp in range(M):
        for total in range(N, 0, -1):
            for curCost in range(1, total+1):
                profit = DP[total-curCost] + data[curCost][curCorp]
                if DP[total] < profit:
                    traceback[total] = traceback[total-curCost] + [(curCorp, curCost)]
                    DP[total] = profit

    # 역추적
    result = array('I', [0]) * (M)
    for corp, cost in traceback[N]:
        result[corp] += cost

    return [[DP[N]], result]


def main():
    N, M = map(int, input().split())
    data = [[0 for _ in range(M)]]
    for _ in range(N):
        _, *b = map(int, input().split())
        data.append(b)

    for i in solve(N, M, data):
        print(*i)


main()
