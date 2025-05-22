# 백준 20312

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
MOD = 1000000007


def solve(N, num):
    result = num[0]
    before = num[0]
    for i in range(1, N-1):
        cur = (before*num[i] + num[i]) % MOD
        result = (result + cur) % MOD
        before = cur

    return result


def main():
    N = int(input())
    num = list(map(int, input().split()))
    print(solve(N, num))


main()
