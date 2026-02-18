# 백준 35265

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(Y, X):
    delete = (Y-1)*(X-1)
    result = [[delete]]

    # (1, 1) ~ (Y-1, X-1)까지 지우기
    for y in range(1, Y):
        for x in range(1, X):
            result.append((y, x))

    # 남은 L에서 퐁당퐁당
    if Y % 2 == 0 and X % 2 == 0:
        # (Y, 1) ~ (Y, X)까지 퐁당퐁당
        for x in range(2, X+1, 2):
            result.append((Y, x))
            result[0][0] += 1
        # (1, X) ~ (Y-1, X)까지 퐁당퐁당
        for y in range(2, Y-1, 2):
            result.append((y, X))
            result[0][0] += 1
    else:
        # (Y, X-1) ~ (Y, 2)까지 퐁당퐁당
        for x in range(X-1, 1, -2):
            result.append((Y, x))
            result[0][0] += 1
        # (Y-1, X) ~ (2, X)까지 퐁당퐁당
        for y in range(Y-1, 1, -2):
            result.append((y, X))
            result[0][0] += 1

    return result


def main():
    T = int(input())
    for _ in range(T):
        Y, X = map(int, input().split())
        for i in solve(Y, X):
            print(*i)


main()
