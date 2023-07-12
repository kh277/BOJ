# 백준 2193

from sys import stdin

input = stdin.readline

'''
1자리 : 1
2자리 : 10
3자리 : 100, 101
4자리 : 1000, 1001, 1010
N자리일 경우, 마지막 자릿수가 1일 경우, N-1은 0이 되어야 함. 따라서 DP[N-2]
마지막 자릿수가 0일 경우, N-1은 제한이 없으므로 DP[N-1]
따라서, 점화식은 DP[N] = DP[N-1] + DP[N-2]이 됨.
'''


def solve(N: int) -> int:
    # DP[N] = N자리 이친수 갯수
    DP = [0 for _ in range(N+1)]
    DP[0] = 0
    DP[1] = 1

    if N > 1:
        DP[2] = 1

    if N > 2:
        for i in range(3, N + 1):
            # 점화식
            DP[i] = DP[i - 1] + DP[i - 2]

    return DP[N]


def main():
    N = int(input())
    print(solve(N))


main()
