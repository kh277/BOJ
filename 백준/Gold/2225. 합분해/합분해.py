# 백준 2225

'''
가로줄을 합을 나타낼 때 사용하는 수의 개수, 세로줄을 합이 j인 수로 DP테이블을 나타내 보자.

DP[i][j] = i개의 수를 사용해서 합이 j인 수를 만드는 경우의 수

DP[3][0]은 (0, 0, 0),
DP[3][1]은 (1, 0, 0), (0, 1, 0), (0, 0, 1),
DP[3][2]는 (2, 0, 0), (0, 2, 0), (1, 1, 0), (1, 0, 1), (0, 1, 1), (0, 0, 2),
...
가 된다.
여기서 잘 살펴보면 (숫자 3개로 합이 2 경우) =
(숫자 2개로 합이 2인 경우) + 1, (숫자 2개로 합이 1인 경우) + 2, (숫자 2개로 합이 0인 경우) + 3이 된다.
따라서 DP[3][2] = DP[2][2] + DP[2][1] + DP[2][0]이 성립한다.

일반화시켜보면,
DP[i][j] = DP[i-1][j] + DP[i-1][j-1] + ... nmu[i-1][0]이 성립한다.

여기서
DP[i-1][j-1] + ... DP[i-1][0] = DP[i][j-1]이므로
DP[i][j] = DP[i][j-1] + DP[i-1][j]가 성립한다.
'''

import sys

input = sys.stdin.readline


def solve(N: int, K: int) -> list:
    DP = [[0 for _ in range(N+1)] for _ in range(K+1)]
    
    # 초기값 설정
    for j in range(N+1):
        DP[1][j] = 1       # 숫자 1개를 사용해서 합이 j인 수를 만드는 가짓수는 항상 1임

    for i in range(K+1):
        DP[i][0] = 1       # 숫자 i개를 사용해서 합이 0인 수를 만드는 가짓수는 항상 1임

    for i in range(2, K+1):
        for j in range(1, N+1):
            DP[i][j] = (DP[i][j-1] + DP[i-1][j]) % 1000000000
        

    return DP[K][N]


def main():
    N, K = map(int, input().split())
    
    print(solve(N, K))


main()