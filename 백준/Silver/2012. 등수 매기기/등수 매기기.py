# 백준 2012

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, A):
    A.sort()

    count = 0
    for i in range(N):
        count += abs(i+1 - A[i])

    return count


def main():
    N = int(input())
    grade = []
    for _ in range(N):
        grade.append(int(input()))
    print(solve(N, grade))


main()
