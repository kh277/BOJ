# 백준 9237

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, tree):
    tree.sort(reverse=True)

    maxDay = 0
    for i in range(1, N+1):
        cur = tree[i-1]
        maxDay = max(maxDay, i+1+cur)
    
    return maxDay


def main():
    N = int(input())
    tree = list(map(int, input().split()))
    print(solve(N, tree))


main()
