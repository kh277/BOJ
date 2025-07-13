# 백준 1439

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(S):
    result = [0, 0]

    result[int(S[0])] += 1
    for i in range(1, len(S)):
        if S[i-1] != S[i]:
            result[int(S[i])] += 1

    return min(result)


def main():
    S = input().decode().rstrip()
    print(solve(S))


main()
