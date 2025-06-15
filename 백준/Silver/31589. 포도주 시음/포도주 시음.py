# 백준 31589

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, K, data):
    data.sort()

    result = 0
    if K % 2 == 0:
        K -= 1

    result += data[N-1]
    for i in range(K//2):
        result += data[N-2-i] - data[i]

    return result


def main():
    N, K = map(int, input().split())
    data = list(map(int, input().split()))
    print(solve(N, K, data))


main()
