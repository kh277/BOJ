# 백준 21650

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, score):
    winScore = max(score)
    winIndex = score.index(winScore)

    # 우승자 이후부터 탐색
    fatherScore = -1
    for i in range(winIndex+1, N-1):
        if score[i] % 10 == 5 and score[i] > score[i+1]:
            fatherScore = max(fatherScore, score[i])

    if fatherScore == -1:
        return 0

    # 등수 추출
    curRank = 1
    for i in score:
        if fatherScore < i:
            curRank += 1

    return curRank


def main():
    N = int(input())
    score = list(map(int, input().split()))
    print(solve(N, score))


main()
