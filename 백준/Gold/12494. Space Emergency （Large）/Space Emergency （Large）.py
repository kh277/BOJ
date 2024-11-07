# 백준 12494

import sys
import heapq

input = sys.stdin.readline

def solve(L, t, N, C, cNum):
    '''
    L : 스피드 부스터 개수
    t : 스피드 부스터 건설 시간
    N : 도착까지 거쳐야 하는 별의 수
    C : 행성 간 거리에서 반복되는 수의 개수
    cNum : 행성 간 거리
    '''
    
    length = []
    for i in range(N):
        length.append(cNum[i%C]*2)
    
    result = 0    # 지나온 거리 저장
    index = 0    # 현재 탐사하는 별의 인덱스
    resultTime = sum(length)    # 도착까지 걸리는 시간
    pq = []
    
    # 부스터가 완성되기 전까지 반복
    while index < N:
        curRange = length[index]
        
        # 이번 여행 중 부스터가 완성될 경우     
        if result + curRange >= t:
            leftRange = result+curRange - t
            result += t - result
            heapq.heappush(pq, -leftRange)
            break
        
        # 부스터가 완성될 때까지 아직 시간이 남은 경우
        result += curRange
        index += 1
    
    # 부스터가 완성되고 남은 거리는 우선순위 큐에 추가
    for i in range(index+1, N):
        heapq.heappush(pq, -length[i])
    
    # 부스터 L회 사용
    for i in range(L):
        if pq:
            resultTime += heapq.heappop(pq)//2
        
    return resultTime


# main 함수 ----------
T = int(input())
for i in range(1, T+1):
    A = list(map(int, input().split()))
    
    print("Case #{a}: {b}".format(a=i, b=solve(A[0], A[1], A[2], A[3], A[4:])))
    