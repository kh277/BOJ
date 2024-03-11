# 백준 10844

'''
1자리 수일때 0, 1, ..., 9로 끝나는 수의 개수는 0, 1, ..., 1이 된다.
2자리 수일때 0으로 끝나는 수의 개수는 1자리 수일때 1로 끝나는 수의 개수와 같다.
2자리 수일때 1로 끝나는 수의 개수는 1자리 수일때 0, 2로 끝나는 수의 개수 합과 같다.
이와 동일한 방식으로 1000x10 크기의 배열을 이용하여 계산한다.

'''

import sys

input = sys.stdin.readline


def solve(N: int) -> int:
    dp = [[0 for _ in range(10)] for _ in range(1002)]
    for i in range(10):
        dp[1][i] = 1
    dp[1][0] = 0

    for i in range(2, N+1):
        # 0, 9에 대한 예외 처리
        dp[i][0] = dp[i-1][1]
        dp[i][9] = dp[i-1][8]
        
        # 일반항
        for j in range(1, 9):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
        
        # 오버플로우 처리
        for j in range(0, 10):
            dp[i][j] = dp[i][j] % 1000000000
    
    # 총합 계산
    sum = 0
    for i in range(0, 10):
        sum += dp[N][i]
    
    return sum % 1000000000


def main():
    N = int(input())
    print(solve(N))
   

main()