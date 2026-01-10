# 백준 35095

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N):
    if N <= 360:
        return 0
    elif N <= 390:
        return N-360
    elif N <= 570:
        return 30
    elif N <= 585:
        return N-540
    elif N <= 645:
        return 45
    else:
        return N-600


def main():
    N = int(input())
    print(solve(N))


main()
