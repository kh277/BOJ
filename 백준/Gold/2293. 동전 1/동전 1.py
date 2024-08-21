# 백준 2293

'''
생각1
그리디하게 선택할 경우 한 가지 해만 찾을 수 있다.
모든 경우의 수를 구해야 하므로 DP를 이용하자.

가로축은 가치(k), 세로축은 동전의 액면가를 기준으로 세우자.
DP[i][j] = 1 ~ i번째까지의 동전을 사용하여 j원을 만들 수 있는 경우의 수.

생각2
이차원 DP를 사용할 경우 메모리 초과가 발생한다.
이전 값까지의 합은 이전 DP에 저장되어 있으므로 일차원 DP로 압축이 가능하다.
'''

import sys

input = sys.stdin.readline


def solve(N: int, K: int, coin: list) -> int:
    DP = [0 for _ in range(K+1)]

    for i in range(1, N+1):
        cur = coin[i-1]     # 현재 동전의 액면가
        for j in range(cur, K+1):
            # cur 동전 1개로 cur 비용을 내는 경우
            if j == cur:
                DP[j] += 1
            # 1~i번째 동전까지 사용하여 j원을 만드는 경우
            else:
                DP[j] += DP[j-cur]

    return DP[K]


def main():
    N, K = map(int, input().split())

    coin = []
    for _ in range(N):
        coin.append(int(input()))
    
    print(solve(N, K, coin))


main()
