# 백준 14658

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(L, K, star):
    star.sort(key= lambda x: (x[0], x[1]))

    result = 0
    for i in range(K):
        for j in range(K):
            startX = star[i][0]
            startY = star[j][1]

            curStar = 0
            for k in range(K):
                if startX <= star[k][0] <= startX+L and startY <= star[k][1] <= startY+L:
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
