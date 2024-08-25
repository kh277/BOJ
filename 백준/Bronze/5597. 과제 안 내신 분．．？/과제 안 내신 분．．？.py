# 백준 10813

import sys

input = sys.stdin.readline


def solve(student: list) -> list:
    DP = [i for i in range(31)]

    for i in student:
        DP[i] = 0

    return [i for i in range(1, 31) if DP[i] != 0]


def main():
    student = []
    for _ in range(28):
        student.append(int(input()))

    for i in solve(student):
        print(i)


main()