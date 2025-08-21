# 백준 14658

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(L, K, star):
    star.sort(key= lambda x: (x[0], x[1]))

    result = 0
    for i in range(K):
        startX, _ = star[i]
        endX = startX + L
        for j in range(K):
            _, startY = star[j]
            endY = startY + L
            curStar = 0
            for k in range(K):
                if startX <= star[k][0] <= endX and startY <= star[k][1] <= endY:
                    curStar += 1
            result = max(result, curStar)

    return K - result


def main():
    X, Y, L, K = map(int, input().split())
    star = []
    for _ in range(K):
        star.append(list(map(int, input().split())))
    print(solve(L, K, star))


main()
