# 백준 3230

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, M, first, second):
    score = []
    for i in range(N):
        score.insert(first[i]-1, i+1)
    
    score2 = []
    score = score[:M][::-1]
    for i in range(M):
        score2.insert(second[i]-1, score[i])
    
    return score2[:3]


def main():
    N, M = map(int, input().split())
    first = []
    for _ in range(N):
        first.append(int(input()))
    second = []
    for _ in range(M):
        second.append(int(input()))
    for i in solve(N, M, first, second):
        print(i)


main()
