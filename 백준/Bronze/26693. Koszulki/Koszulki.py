# 백준 26693

import sys

input = sys.stdin.readline


def solve():
    score.sort(reverse=True)
    index = K-1
    temp = score[index]

    while True:
        if index >= N:
            break
        if score[index] != temp:
            break
        index += 1
    
    return index


# main 함수 ----------
N, K = map(int, input().split())
score = list(map(int, input().split()))
print(solve())