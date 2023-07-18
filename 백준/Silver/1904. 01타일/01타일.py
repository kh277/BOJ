# 백준 1904

'''
N=1; 1
N=2; 00, 11
N=3; 001, 111, 100
N=4; 0011, 1111, 1001, 0000, 1100
'''

from sys import stdin

input = stdin.readline


def solve(N: int) -> int:
    # DP[N] = 길이가 N인 모든 2진 수열의 개수 % 15746
    DP = [0 for _ in range(N+1)]
    DP[0] = 0
    DP[1] = 1

    if N > 1:
        DP[2] = 2
    if N > 2:
        for i in range(3, N+1):
            DP[i] = (DP[i-1] + DP[i-2]) % 15746

    return DP[N]


def main():
    N = int(input())
    print(solve(N))


main()