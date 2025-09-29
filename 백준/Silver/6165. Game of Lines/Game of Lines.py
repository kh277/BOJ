# 백준 6165

import io
import math

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, point):
    point.sort(key= lambda x: (x[0], x[1]))
    result = 0
    slope = dict()
    for i in range(N-1):
        ax, ay = point[i]
        for j in range(i+1, N):
            bx, by = point[j]
            gcd = math.gcd(abs(by-ay), abs(bx-ax))
            if gcd == 0:
                gcd = 1
            cur = ((by-ay)//gcd, (bx-ax)//gcd)

            if cur in slope:
                continue
            else:
                slope[cur] = 1
                result += 1

    return result


def main():
    N = int(input())
    point = []
    for _ in range(N):
        point.append(list(map(int, input().split())))

    print(solve(N, point))


main()
