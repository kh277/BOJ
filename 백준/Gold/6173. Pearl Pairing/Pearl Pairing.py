# 백준 6173

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
ARRAY_TYPE = 'i'


def solve(N, pearl):
    half = N//2
    result = array(ARRAY_TYPE, [0]) * N

    index = 0
    pearlIndex = 0
    for i in pearl:
        for _ in range(i):
            result[index] += pearlIndex+1
            index += 1
        pearlIndex += 1
    
    return [(result[i], result[i+half]) for i in range(half)]


def main():
    N, C = map(int, input().split())
    pearl = array(ARRAY_TYPE)
    for _ in range(C):
        pearl.append(int(input()))
    for i in solve(N, pearl):
        print(*i)


main()
