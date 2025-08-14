# 백준 11004

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def main():
    N, K = map(int, input().split())
    print(sorted(list(map(int, input().split())))[K-1])


main()
