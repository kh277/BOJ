# 백준 12851

import sys
from collections import deque

input = sys.stdin.readline


def BFS(start: int, end: int) -> list:
    # 예외 처리
    if start == end:
        return [0, 1]
    
    visited = set()
    q = deque()
    q.append([start, 0])
    
    result = [10e7, 0]
    while q:
        curX, curTime = q.popleft()
        visited.add(curX)
        
        nextX = [curX-1, curX+1, curX*2]
        for i in range(3):
            # 목표에 도달했다면
            if nextX[i] == end:
                if result[0] > curTime+1:
                    result = [curTime+1, 1]
                elif result[0] == curTime+1:
                    result[1] = result[1]+1
                    
            # 이후 탐색
            elif 0 <= nextX[i] <= 100000 and nextX[i] not in visited:
                if curTime > result[0]:
                    continue
                q.append([nextX[i], curTime+1])
                
    return result


def main():
    N, K = map(int, input().split())

    for i in BFS(N, K):
        print(i)


main()