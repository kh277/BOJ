# 백준 1966

import sys
from collections import deque

input = sys.stdin.readline


def solve():
    # [중요도, 인덱스] 순서로 저장
    data = [[importance[i], i] for i in range(N)]
    importance.sort()
    count = 1
    q = deque(data)

    while q:
        curImp, curIndex = q.popleft()
        if importance[-1] != curImp:
            q.append([curImp, curIndex])
            continue
        else:
            importance.pop()
        if curIndex == M:
            return count
        count += 1


# main 함수 ----------
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())

    importance = list(map(int, input().split()))
    print(solve())
