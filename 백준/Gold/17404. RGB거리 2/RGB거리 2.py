# 백준 17404

'''
1149번 RGB 거리 문제에서
"k번째 집은 k-1번째, k+1번째 집과 색이 달라야 한다"는 조건만 추가된 문제이다.

k번째 집과 k+1번째 집의 색이 다르면
자동적으로 k+1번째 집은 k번째 집, k+2번째 집과는 색이 다르게 된다.

결국 제일 마지막 N번째 집과 N-1번째 집, 1번째 집과 색이 다르다는 부분만 신경써주면 된다.
따라서 1번째 집의 색이 R일 때, G일 때, B일 때로 고정시키고 DP를 진행하자.
'''

import sys

input = sys.stdin.readline
INF = 10e7


def solve(N: int, cost: list) -> int:
    DP = [[0, 0, 0] for _ in range(N)]

    # 첫 번째 집의 색이 R일 때
    DP[0] = [cost[0][0], INF, INF]

    for i in range(1, N):
        DP[i][0] = cost[i][0] + min(DP[i-1][1], DP[i-1][2])
        DP[i][1] = cost[i][1] + min(DP[i-1][0], DP[i-1][2])
        DP[i][2] = cost[i][2] + min(DP[i-1][0], DP[i-1][1])
    
    result = min(DP[N-1][1], DP[N-1][2])

    # 첫 번째 집의 색이 G일 때
    DP[0] = [INF, cost[0][1], INF]

    for i in range(1, N):
        DP[i][0] = cost[i][0] + min(DP[i-1][1], DP[i-1][2])
        DP[i][1] = cost[i][1] + min(DP[i-1][0], DP[i-1][2])
        DP[i][2] = cost[i][2] + min(DP[i-1][0], DP[i-1][1])
    
    result = min(result, DP[N-1][0], DP[N-1][2])


    # 첫 번째 집의 색이 B일 때
    DP[0] = [INF, INF, cost[0][2]]

    for i in range(1, N):
        DP[i][0] = cost[i][0] + min(DP[i-1][1], DP[i-1][2])
        DP[i][1] = cost[i][1] + min(DP[i-1][0], DP[i-1][2])
        DP[i][2] = cost[i][2] + min(DP[i-1][0], DP[i-1][1])
    
    return min(result, DP[N-1][0], DP[N-1][1])


def main():
    N = int(input())
    cost = []
    for i in range(N):
        cost.append(list(map(int, input().split())))

    print(solve(N, cost))


main()
