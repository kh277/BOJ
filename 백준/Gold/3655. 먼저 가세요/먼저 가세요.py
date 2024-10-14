# 백준 3655

'''
가장 마지막 친구가 오는 시각이 빠른 순서대로 정렬하면 된다.

절약하는 전체 시간은 (원래 기다려야 하는 시간) - (정렬한 뒤 기다려야 하는 시간)으로 구하면 된다.
'''

import sys

input = sys.stdin.readline


# 리스트 L에서 그룹의 마지막 친구 위치 반환 
def getLastPos(L):
    # 마지막 친구의 위치 저장
    dic = dict()
    for i in range(N-1, -1, -1):
        if L[i] not in dic:
            # [문자, 마지막 등장 인덱스, 등장 빈도수]
            dic[L[i]] = [L[i], i, 1]
        else:
            dic[L[i]][2] += 1

    # 마지막 나온 순서대로 정렬
    return sorted(list(dic.values()), key= lambda x: x[1])


# 리스트 waiting에서 마지막 친구의 위치를 저장한 리스트 L을 참고하여
# 사람들이 기다려야 하는 총 시간 계산
def calWaiting(waiting):
    result = 0
    
    dic = dict()
    for i in range(N):
        if waiting[i] not in dic:
            dic[waiting[i]] = [i]
        else:
            dic[waiting[i]].append(i)
    
    for cur in dic.values():
        for i in range(len(cur)-1):
            result += cur[-1] - cur[i]
    
    return result*5


def solve():
    # waiting에서 마지막 친구의 위치 저장
    lastPos = getLastPos(waiting)
    
    # 정렬 후 마지막 친구가 빨리 오는 그룹 배치
    sortWaiting = []
    for i in range(len(lastPos)):
        name, pos, freq = lastPos[i]
        sortWaiting.extend([name] * freq)
    
    sortLastPos = getLastPos(sortWaiting)
    
    return calWaiting(waiting) - calWaiting(sortWaiting)


# main 함수 ----------
T = int(input())
for _ in range(T):
    N = int(input())
    waiting = list(input().rstrip())
    
    print(solve())