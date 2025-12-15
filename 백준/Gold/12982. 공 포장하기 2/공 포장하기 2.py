# 백준 12982

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(K, X):
    box = 0

    # 같은 색 공을 K개씩 묶고 남은 공 저장 
    ball = []
    for i in range(K):
        box += X[i] // K
        left = X[i] % K
        if left > 0:
            ball.append(left)

    if len(ball) == 0:
        return box

    # [0, i-1]까지는 같은 색끼리, [i, len(ball)]까지는 다른 색끼리 박스에 담기
    ball.sort(reverse=True)
    total = len(ball)
    for i in range(len(ball)):
        total = min(total, i+ball[i])

    return box + total


def main():
    K = int(input())
    X = list(map(int, input().split()))
    print(solve(K, X))


main()
