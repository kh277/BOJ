# 백준 2966

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, string):
    A = "ABC" * 34
    B = "BABC" * 25
    C = "CCAABB" * 17
    score = [0, 0, 0]

    for i in range(N):
        if A[i] == string[i]:
            score[0] += 1
        if B[i] == string[i]:
            score[1] += 1
        if C[i] == string[i]:
            score[2] += 1
    
    result = []
    maxScore = max(score)
    if score[0] == maxScore:
        result.append("Adrian")
    if score[1] == maxScore:
        result.append("Bruno")
    if score[2] == maxScore:
        result.append("Goran")
    
    return [maxScore] + sorted(result)


def main():
    N = int(input())
    string = input().decode().rstrip()
    for i in solve(N, string):
        print(i)


main()
