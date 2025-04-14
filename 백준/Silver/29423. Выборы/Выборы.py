# 백준 29423

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, num):
    arr = array('i', [1]) * (N+1)
    arr[0] = 0

    for curNum in num:
        if arr[curNum] == 0:
            continue

        coef = 1
        while coef*curNum <= N:
            arr[coef*curNum] = 0
            coef += 1
    
    return sum(arr)


def main():
    N, K = map(int, input().split())
    num = list(map(int, input().split()))
    print(solve(N, num))


main()
