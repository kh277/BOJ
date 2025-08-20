# 백준 11540

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, solveA, solveB):
    canSolve = [solveA, solveB]
    revCount1 = 0
    revCount2 = 0
    curUse1 = 0
    curUse2 = 1
    for i in sorted(solveA | solveB):
        if i not in canSolve[curUse1] and i in canSolve[curUse1^1]:
            curUse1 ^= 1
            revCount1 += 1
        if i not in canSolve[curUse2] and i in canSolve[curUse2^1]:
            curUse2 ^= 1
            revCount2 += 1

    return min(revCount1, revCount2)


def main():
    N, A, B = map(int, input().split())
    solveA = set(map(int, input().split()))
    solveB = set(map(int, input().split()))
    print(solve(N, solveA, solveB))


main()
