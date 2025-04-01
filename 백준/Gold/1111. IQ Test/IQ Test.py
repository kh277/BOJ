# 백준 1111

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, num):
    if N == 1:
        return 'A'
    elif N == 2:
        if num[0] == num[1]:
            return num[0]
        return 'A'

    a = 0
    if num[1] - num[0] != 0:
        a = (num[2] - num[1]) // (num[1] - num[0])
    b = num[1] - num[0]*a

    result = num[0]
    for i in range(1, N+1):
        result = result * a + b
        if i < N and result != num[i]:
            return 'B'

    return result


def main():
    N = int(input())
    num = list(map(int, input().split()))
    print(solve(N, num))


main()