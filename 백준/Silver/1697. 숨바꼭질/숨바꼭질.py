# 백준 1697

'''
시작점으로부터 +1, -1, ×2를 한 숫자에 대해 걸린 수를 저장한다.
BFS를 이용하여 시작점부터 탐색하여 목표에 도달할 때까지 탐색한다.
'''

import sys
from collections import deque

input = sys.stdin.readline


def solve(start: int, end: int) -> int:
    visited = [False for _ in range(100005)]
    q = deque()
    q.append([start, 0])

    while q:
        temp = q.popleft()

        # 이미 방문한 노드라면
        if visited[temp[0]]:
            continue

        # 방문한 표시
        visited[temp[0]] = True

        # 종료 조건 확인
        if temp[0] == end:
            return temp[1]

        # 현재 수 - 1
        if temp[0] - 1 >= 0:
            case1 = temp[0] - 1
            q.append([case1, temp[1] + 1])

        # 현재 수 + 1
        if temp[0] + 1 <= 100000:
            case2 = temp[0] + 1
            q.append([case2, temp[1] + 1])

        # 현재 수 * 2
        if temp[0] * 2 <= 100000:
            case3 = temp[0] * 2
            q.append([case3, temp[1] + 1])


def main():
    N, K = map(int, input().split())

    print(solve(N, K))


main()
