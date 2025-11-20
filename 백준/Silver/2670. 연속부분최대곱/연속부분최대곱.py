# 백준 2670

'''
DP[i] = i번째 수를 반드시 포함한 경우, 연속한 부분곱의 최대값
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, num):
    DP = [0 for _ in range(N)]
    DP[0] = num[0]

    for i in range(1, N):
        DP[i] = max(DP[i-1]*num[i], num[i])

    maxV = 0
    for i in range(N):
        if DP[i] > maxV:
            maxV = DP[i]

    return f"{maxV:.3f}"


def main():
    N = int(input())
    num = []
    for _ in range(N):
        num.append(float(input()))

    print(solve(N, num))


main()
