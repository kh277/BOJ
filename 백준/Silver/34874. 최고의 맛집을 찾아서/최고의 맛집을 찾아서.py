# 백준 34874

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(Y, X, student):
    maxScore = [max(i) for i in student]
    needFix = [0 for _ in range(X)]
    for y in range(Y):
        for x in range(X):
            if maxScore[y] > student[y][x]:
                needFix[x] += 1

    return needFix


def main():
    Y, X = map(int, input().split())
    student = []
    for _ in range(Y):
        student.append(list(map(int, input().split())))
    print(*solve(Y, X, student))


main()
