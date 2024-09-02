# 백준 1354

'''
1351번과 유사하다.
'''

import sys

input = sys.stdin.readline


def recur(N: int, P: int, Q: int, X: int, Y: int, DP: dict) -> int:
    if N <= 0:
        return 1

    if N//P-X not in DP:
        DP[N//P-X] = recur(N//P-X, P, Q, X, Y, DP)
    if N//Q-Y not in DP:
        DP[N//Q-Y] = recur(N//Q-Y, P, Q, X, Y, DP)

    return DP[N//P-X] + DP[N//Q-Y]


def main():
    N, P, Q, X, Y = map(int, input().split())
    print(recur(N, P, Q, X, Y, dict()))
    

main()