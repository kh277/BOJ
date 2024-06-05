# 백준 2847

import sys

input = sys.stdin.readline

def solve(N, score):
    cur = score[N-1]
    count = 0

    for i in range(N-2, -1, -1):
        if score[i] >= cur:
            count += score[i] - (cur - 1)
            score[i] = cur - 1
            cur = score[i]
        else:
            cur = score[i]

    return count


def main():
    N = int(input())

    score = []
    for _ in range(N):
        score.append(int(input()))

    print(solve(N, score))


main()