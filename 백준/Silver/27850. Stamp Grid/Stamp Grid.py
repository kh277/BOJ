# 백준 27850

import sys

input = sys.stdin.readline


# stamp를 start위치에 찍었을 때 target과 일치하는지 확인
def isCorrect(K, target, stamp, start):
    for i in range(K):
        for j in range(K):
            if stamp[i][j] == '*':
                if target[start[0]+i][start[1]+j] == '.':
                    return False
    
    return True


def solve(N, K, target, stamp):
    curState = [['.' for _ in range(N)] for _ in range(N)]
    stampRotate = [stamp]

    # 각 스탬프를 90도씩 회전시킨 상태 저장
    for i in range(1, 4):
        temp = [['.' for _ in range(K)] for _ in range(K)]
        for y in range(K):
            for x in range(K):
                temp[y][x] = stampRotate[-1][K-x-1][y]
        stampRotate.append(temp)

    # 스탬프를 한 칸씩 옮겨가며 비교
    for y in range(N-K+1):
        for x in range(N-K+1):
            for case in range(4):
                # 현재 stamp의 모형이 스탬프 그림의 일부분과 완전 일치한다면 curState에 저장
                if isCorrect(K, target, stampRotate[case], [y, x]) == True:
                    for i in range(K):
                        for j in range(K):
                            if stampRotate[case][i][j] == '*':
                                curState[y+i][x+j] = stampRotate[case][i][j]
    
    # 완성된 curState가 target과 일치하는지 확인
    for y in range(N):
        for x in range(N):
            if target[y][x] == '*':
                if curState[y][x] != '*':
                    return 'NO'
    
    return 'YES'


# main 함수 ----------
T = int(input())
for _ in range(T):
    blank = input()
    N = int(input())
    target = []
    for _ in range(N):
        target.append(list(input().rstrip()))
    K = int(input())
    stamp = []
    for _ in range(K):
        stamp.append(list(input().rstrip()))
    
    print(solve(N, K, target, stamp))