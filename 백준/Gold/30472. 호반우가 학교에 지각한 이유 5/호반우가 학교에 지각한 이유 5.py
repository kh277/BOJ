# 백준 30472

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, card):
    card.sort(key= lambda x: (x[1]-x[0]))

    ground = 0
    curH = 0
    accH = 0
    for i in range(N):
        u, d = card[i]
        curH += u
        accH += curH
        curH -= d
        ground = min(ground, curH)

    return accH - ground*N


def main():
    N = int(input())
    card = []
    for _ in range(N):
        card.append(tuple(map(int, input().split())))

    print(solve(N, card))


main()
