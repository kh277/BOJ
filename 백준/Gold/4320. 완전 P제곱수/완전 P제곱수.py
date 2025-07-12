# 백준 4320

import io
import math

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N):
    isMinus = False
    if N < 0:
        N *= -1
        isMinus = True

    for i in range(2, math.ceil(math.sqrt(N))+1):
            temp = i
            count = 1
            while temp < N:
                if N % temp == 0:
                    count += 1
                    temp *= i
                else:
                    break

            if temp == N:
                if isMinus == False:
                    return count
                if isMinus == True and count % 2 == 1:
                    return count

    return 1


def main():
    while True:
        N = int(input())
        if N == 0:
            break
        print(solve(N))


main()
