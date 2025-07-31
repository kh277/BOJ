# 백준 1876

import io
import math

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(T, X):
    radX = math.radians(X)
    sinX = math.sin(radX)
    tanX = math.tan(radX)

    curD = 0
    left = T - 16/sinX
    right = T + 16/sinX

    while curD < right:
        if left < curD < right:
            return 'yes'
        curD += 85/tanX
    
    return 'no'


def main():
    T = int(input())
    for _ in range(T):
        T, X = map(float, input().split())
        print(solve(100*T, X))


main()
