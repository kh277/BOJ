# 백준 10039

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(score):
    for i in range(5):
        if score[i] < 40:
            score[i] = 40
    return sum(score)//5


def main():
    score = []
    for _ in range(5):
        score.append(int(input()))
    print(solve(score))


main()
