# 백준 28292

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def main():
    N = int(input())
    if N in {1, 2}:
        print(1)
    elif N in {3, 4, 5}:
        print(2)
    else:
        print(3)


main()
