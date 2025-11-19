# 백준 1409

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


# 회전각이 theta일 때, start에서 시작해서 이어질 수 있는 모든 간선의 수 체크
def DFS(N, setP, visited, start, theta):
    count = 1
    stack = []
    stack.append(start)
    visited.add(start)

    while stack:
        curV = stack.pop()

        for nextV in [(curV+theta)%360, (curV-theta)%360]:
            if nextV in setP and nextV not in visited:
                stack.append(nextV)
                visited.add(nextV)
                count += 1

    return count


def solve(N, point):
    if N == 1:
        return 0

    # 두 점 사이의 간격 전부 구하기
    gap = set()
    for i in range(N-1):
        for j in range(i+1, N):
            gap.add(point[j]-point[i])

    maxMatch = 0
    setP = set(point)

    # 모든 회전각 theta에 대해 최대 매칭 수 체크
    for theta in gap:
        visited = set()
        curMatch = 0
        for i in range(N):
            if point[i] in setP and point[i] not in visited:
                curMatch += DFS(N, setP, visited, point[i], theta) // 2
        maxMatch = max(maxMatch, curMatch)

    return maxMatch * 2


def main():
    N = int(input())
    point = []
    for _ in range(N):
        point.append(int(input()))

    print(solve(N, point))


main()
