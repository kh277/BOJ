# 백준 19942

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def check(leftIngred):
    for i in range(4):
        if leftIngred[i] > 0:
            return False

    return True


def backtrack(curNum, leftIngred, curCost, curInclude):
    global minCost, minSet

    # 종료 조건 체크
    if check(leftIngred) == True:
        if minCost > curCost:
            minCost = curCost
            minSet = curInclude
        return

    # 이후 탐색
    for i in range(curNum+1, N):
        if i not in curInclude:
            left = [leftIngred[j]-ingred[i][j] for j in range(4)]
            backtrack(i, left, curCost+ingred[i][4], curInclude | {i})


# main 함수 ----------
N = int(input())
need = list(map(int, input().split()))
ingred = []
for _ in range(N):
    ingred.append(list(map(int, input().split())))

minCost = 10000
minSet = []
backtrack(-1, need, 0, set())

if minCost == 10000:
    print(-1)
else:
    print(minCost)
    print(*[i+1 for i in minSet])
