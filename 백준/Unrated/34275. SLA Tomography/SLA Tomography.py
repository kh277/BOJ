# 백준 34275

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, data):
    result = 1
    prevH = 0
    for i in range(N):
        if data[i] > prevH:
            result += data[i]-prevH+1
        prevH = data[i]

    return result


def main():
    N = int(input())
    data = array('I')
    for _ in range(N):
        data.append(int(input()))
    print(solve(N, data))


main()
