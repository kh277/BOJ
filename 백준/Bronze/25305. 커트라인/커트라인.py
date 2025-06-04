# 백준 25305

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, K, score):
    score.sort(reverse=True)
    return score[K-1]


def main():
    N, K = map(int, input().split())
    score = list(map(int, input().split()))

    print(solve(N, K, score))


main()
