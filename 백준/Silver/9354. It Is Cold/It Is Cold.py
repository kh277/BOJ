# 백준 9354

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, S, C):
    accSum = 0
    index = N-1
    isT = False
    while index >= 0:
        if isT == False:
            if C[index] == 'T':
                isT = True
                accSum += S[index]
        else:
            if C[index] == 'A':
                accSum -= S[index]
                if accSum < 0:
                    accSum = 0
            else:
                accSum += S[index]
        index -= 1

    return accSum


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        S = list(map(int, input().split()))
        C = list(input().decode().rstrip().split())
        print(solve(N, S, C))


main()
