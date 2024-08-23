# 백준 15992

'''
가로축은 나타낼 정수, 세로축은 사용한 숫자의 개수로 DP 테이블을 구성하면 된다.
DP[i][j] = (1, 2, 3) 중 i개를 사용해서 합이 j인 숫자를 만드는 방법의 수
'''

import sys

input = sys.stdin.readline


def solve(N: int, M: int) -> int:
    DP = [[0 for _ in range(N+1)] for _ in range(M+1)]

    # 초기값 설정
    if N >= 1:
        DP[1][1] = 1
        if N >= 2:
            DP[1][2] = 1
            if N >= 3:
                DP[1][3] = 1

    # 이후 값에 대해 DP 처리
    for i in range(2, M+1):
        for j in range(i, N+1):
            if j > N:
                continue
            if i == j:
                DP[i][j] = 1
            else:
                DP[i][j] = (DP[i-1][j-1] + DP[i-1][j-2] + DP[i-1][j-3]) % 1000000009

    return DP[M][N]


def main():
    T = int(input())
    for _ in range(T):
        n, m = map(int, input().split())

        print(solve(n, m))


main()