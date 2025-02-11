# 백준 3980

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


# curPlayer번째 선수 배정 후 재귀, 이미 배정된 위치는 exceptPos에 저장.
def backtrack(curPlayer, exceptPos, curScore):
    if curPlayer == 11:
        return curScore
    
    # curPlayer번째 선수를 pos위치에 배치
    maxScore = 0
    for nextPos in range(11):
        if nextPos not in exceptPos and stat[curPlayer][nextPos] != 0:
            temp = backtrack(curPlayer+1, exceptPos | {nextPos}, curScore+stat[curPlayer][nextPos])
            if temp != 0:
                maxScore = max(maxScore, temp)

    return maxScore


# main 함수 ----------
T = int(input())
for _ in range(T):
    stat = []
    for _ in range(11):
        stat.append(list(map(int, input().split())))
    print(backtrack(0, set(), 0))