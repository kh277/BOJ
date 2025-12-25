# 백준 15436

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, K):
    if (N-1).bit_length() <= K:
        return "Your wish is granted!"
    return "You will become a flying monkey!"


def main():
    N, K = map(int, input().split())
    print(solve(N, K))


main()
