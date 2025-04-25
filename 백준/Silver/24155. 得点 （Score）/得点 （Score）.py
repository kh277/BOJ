# 백준 24155

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, score):
    score.sort(reverse=True)
    score[0][2] = 1

    for i in range(1, N):
        if score[i][0] == score[i-1][0]:
            score[i][2] = score[i-1][2]
        else:
            score[i][2] = i+1

    score.sort(key= lambda x: (x[1]))
    return [i[2] for i in score]


def main():
    N = int(input())
    score = []
    for i in range(1, N+1):
        score.append([int(input()), i, None])
    for i in solve(N, score):
        print(i)


main()
