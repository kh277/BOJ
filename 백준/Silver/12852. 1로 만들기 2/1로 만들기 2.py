# 백준 12852

import sys
from collections import deque

input = sys.stdin.readline


def solve():
    DP = [0 for _ in range(N+1)]
    visited = [False for _ in range(N+1)]

    DP[N] = 0
    
    q = deque()
    q.append([N, 0, [N]])
    visited[N] = True

    while q:
        cur, curCount, curVisit = q.popleft()
        # 종료조건
        if cur == 1:
            return [[curCount], curVisit]

        # 이후 탐색 체크
        if cur % 3 == 0 and visited[cur//3] == False:
            q.append([cur//3, curCount+1, curVisit + [cur//3]])
            visited[cur//3] = True
        if cur % 2 == 0 and visited[cur//2] == False:
            q.append([cur//2, curCount+1, curVisit + [cur//2]])
            visited[cur//2] = True
        if cur - 1 > 0 and visited[cur-1] == False:
            q.append([cur-1, curCount+1, curVisit + [cur-1]])
            visited[cur-1] = True


# main 함수 ----------
N = int(input())
for i in solve():
    print(*i)