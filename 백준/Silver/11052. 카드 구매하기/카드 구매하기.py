# 백준 11052

'''
그리디 알고리즘으로 해결할 경우
5
1 50 60 100 1
위의 반례를 해결하지 못한다.
즉, 4장+1장을 사는게 아니라 2장+3장을 사야 최적해가 보장된다.

DP를 이용해서 해결하자.
가로축(j)은 카드의 개수(N), 세로축(i)은 카드팩에 들어있는 카드의 개수로 두면 된다.
DP[i][j] = (1~i번째 팩까지 고려할 때, j장의 카드를 사기 위해 지불하는 금액)
'''

import sys

input = sys.stdin.readline


def solve(N: int, P: list) -> int:
    DP = [[0 for _ in range(N+1)] for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(1, N+1):
            if j-i < 0:
                DP[i][j] = DP[i-1][j]
            else:
                DP[i][j] = max(DP[i-1][j], DP[i][j-i]+P[i-1])

    return DP[-1][-1]


def main():
    N = int(input())
    P = list(map(int, input().split()))
    
    print(solve(N, P))


main()