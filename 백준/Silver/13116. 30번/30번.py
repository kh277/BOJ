# 백준 13116

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(A, B):
    resultA = []
    while A > 1:
        if A % 2 == 0:
            resultA.append(0)
        else:
            resultA.append(1)
        A //= 2
    resultA = resultA[::-1]

    resultB = []
    while B > 1:
        if B % 2 == 0:
            resultB.append(0)
        else:
            resultB.append(1)
        B //= 2
    resultB = resultB[::-1]

    result = 1
    for i in range(min(len(resultA), len(resultB))):
        if resultA[i] == resultB[i]:
            if resultA[i] == 0:
                result = result*2
            else:
                result = result*2 + 1
        else:
            break

    return result*10


def main():
    T = int(input())
    for _ in range(T):
        A, B = map(int, input().split())
        print(solve(A, B))


main()
