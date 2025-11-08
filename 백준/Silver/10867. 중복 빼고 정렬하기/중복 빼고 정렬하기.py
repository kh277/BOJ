# 백준 10867

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(*sorted(list(set((A)))))


main()
