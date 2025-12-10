# 백준 5545

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, A, B, C, kcal):
    kcal.sort(reverse=True)

    accCost = A
    accKcal = C
    result = accKcal//accCost

    for i in range(N):
        accCost += B
        accKcal += kcal[i]
        result = max(result, accKcal//accCost)
    
    return result


def main():
    N = int(input())
    A, B = map(int, input().split())
    C = int(input())
    kcal = []
    for _ in range(N):
        kcal.append(int(input()))

    print(solve(N, A, B, C, kcal))


main()
