# 백준 2294

'''
2293번과 비슷하나, 액면가가 같은 금액이 주어질 수도 있다.
또한 목표 값 K원을 만드는 모든 경우의 수가 아니라 최소 개수이다.
동전은 몇 개라도 사용할 수 있기 때문에 액면가가 같은 금액은 1개만 남겨도 된다.

DP 테이블의 가로축은 목표 금액 K, 세로축은 동전의 액면가이다.
'''

import sys

input = sys.stdin.readline
INF = 10e5


def solve(N: int, K: int, coin: list) -> int:
    DP = [[INF for _ in range(K+1)] for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(1, K+1):
            if coin[i] == j:
                DP[i][j] = 1
            elif j-coin[i] < 0:
                DP[i][j] = DP[i-1][j]
            else:
                DP[i][j] = min(DP[i-1][j], DP[i][j-coin[i]]+1)

    return DP[N][K] if not DP[N][K] == INF else -1  


def main():
    N, K = map(int, input().split())

    coin = [0]      # 0번 코인은 미사용
    for _ in range(N):
        coin.append(int(input()))
    
    print(solve(N, K, coin))


main()
