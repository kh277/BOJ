# 백준 1092

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve():
    crane.sort(reverse=True)
    boxWeight.sort(reverse=True)
    moved = [False for _ in range(M)]
    
    curMoveCount = 0
    phase = 0
    while True:
        boxIndex = 0
        for i in range(N):
            curCraneLimit = crane[i]

            # i번째 크레인이 옮길 수 있는 박스 탐색
            while boxIndex < M:
                # boxIndex번째 상자를 옮길 수 있을 경우
                if curCraneLimit >= boxWeight[boxIndex] and moved[boxIndex] == False:
                    moved[boxIndex] = True
                    boxIndex += 1
                    curMoveCount += 1
                    break
                boxIndex += 1
        
        # 더 이상 상자를 옮길 수 없을 경우
        if curMoveCount == 0:
            break

        phase += 1
        curMoveCount = 0
    
    for i in moved:
        if i == False:
            return -1
    
    return phase


# main 함수 ----------
N = int(input())
crane = list(map(int, input().split()))
M = int(input())
boxWeight = list(map(int, input().split()))

print(solve())