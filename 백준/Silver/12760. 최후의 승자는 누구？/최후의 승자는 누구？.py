# 백준 12760

'''
각 플레이어가 가진 카드를 오름차순 정렬한 뒤, 큰 카드부터 내도록 하여 승자를 정한다.
'''

import sys

input = sys.stdin.readline


def solve():
    # 각 플레이어의 카드 정렬
    for i in range(N):
        data[i].sort()
    
    score = [0 for _ in range(N)]

    # 라운드 진행
    for rou in range(M):
        maxNum = [0, []]
        for player in range(N):
            if data[player][rou] > maxNum[0]:
                maxNum = [data[player][rou], [player]]
            elif data[player][rou] == maxNum[0]:
                maxNum[1].append(player)
        
        for j in maxNum[1]:
            score[j] += 1
    
    result = []
    maxScore = max(score)
    for i in range(N):
        if maxScore == score[i]:
            result.append(i+1)
    
    return result


# main 함수 ----------
N, M = map(int, input().split())
data = []
for _ in range(N):
    data.append(list(map(int, input().split())))

print(*solve())
