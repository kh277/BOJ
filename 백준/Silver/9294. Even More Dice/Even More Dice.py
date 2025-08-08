# 백준 9294

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, M, S):
    result = []
    stack = []
    for i in range(M, 0, -1):
        stack.append([i])
    
    while stack:
        curP = stack.pop()

        if len(curP) == N:
            if sum(curP) == S:
                result.append(curP)
            continue

        for nextN in range(M, curP[-1]-1, -1):
            temp = curP[:]
            stack.append(temp + [nextN])

    return result


def main():
    T = int(input())
    for i in range(T):
        N, M, S = map(int, input().split())
        print(f"Case {i+1}:")
        for j in solve(N, M, S):
            print('(' + ','.join(map(str, j)) + ')')


main()
