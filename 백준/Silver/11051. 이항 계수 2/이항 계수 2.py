# 백준 11057

'''
이항 계수 (n|k)는 조합 nCk를 의미한다.
이것을 직접 계산하려면 팩토리얼을 계산해야 하므로 시간 초과가 발생하게 된다.

이항 계수 성질 중에 
(n|k) = (n-1|k-1) + (n-1|k)의 성질이 있다.
위 과정을 통해 파스칼 삼각형을 구하면 된다.

가로줄을 K, 세로줄을 N으로 하여 DP 테이블을 구성하자.
'''

import sys

input = sys.stdin.readline


def solve(N: int, K: int) -> int:
    DP = [[0 for _ in range(N+1)] for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(i+1):
            # 파스칼 삼각형에서 값이 1인 이항계수들
            if i == j or j == 0:
                DP[i][j] = 1
            # 점화식
            else:
                DP[i][j] = (DP[i-1][j-1] + DP[i-1][j]) % 10007

            # 탈출조건
            if i == N and j == K:
                return DP[i][j]


def main():
    N, K = map(int, input().split())
    
    print(solve(N, K))


main()