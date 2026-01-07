# 백준 34588

'''
"번호가 i 이하인 돌만 이동시켜서 모든 돌을 직사각형 밖으로 빼낼 수 있는가?"를 결정 문제로 잡고,
매개변수 탐색으로 최소 에너지를 구하면 된다.
'''

import io
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 돌을 움직일 필요가 없는지 체크
def needMove(grid, sqY, sqX):
    for y in range(sqY[0], sqY[1]+1):
        for x in range(sqX[0], sqX[1]+1):
            if grid[y][x] > 0:
                return True
    return False


# mid 이하의 돌만 이동시켜 y=sqY, x=sqX 범위 내의 돌을 전부 밖으로 이동시킬 수 있는지 체크 
def checkBFS(Y, X, grid, mid, sqY, sqX):
    zero = 0
    num = 0
    visited = [[0 for _ in range(X)] for _ in range(Y)]
    q = deque()

    # 초기값 추가
    for y in range(sqY[0], sqY[1]+1):
        for x in range(sqX[0], sqX[1]+1):
            if 0 < grid[y][x] <= mid:
                num += 1
            elif grid[y][x] == 0:
                zero += 1
            else:
                return False
            q.append((y, x))
            visited[y][x] = 1

    while q:
        curY, curX = q.popleft()

        for i in range(4):
            nextX = curX + dx[i]
            nextY = curY + dy[i]

            if 0 <= nextX < X and 0 <= nextY < Y and visited[nextY][nextX] == 0:
                if 0 < grid[nextY][nextX] <= mid:
                    num += 1
                elif grid[nextY][nextX] == 0:
                    zero += 1
                else:
                    continue
                q.append((nextY, nextX))
                visited[nextY][nextX] = 1

    sq = (sqY[1]-sqY[0]+1)*(sqX[1]-sqX[0]+1)
    if zero >= sq:
        return True
    return False


def solve(Y, X, K, grid, sqY, sqX):
    # 움직일 필요가 없는 경우 체크
    if needMove(grid, sqY, sqX) == False:
        return 0

    # 에너지가 K여도 다 못 빼는 경우 체크
    if checkBFS(Y, X, grid, K, sqY, sqX) == False:
        return -1

    # 매개 변수 탐색으로 최소 에너지값 찾기
    no = 0
    yes = K
    while abs(yes-no) > 1:
        mid = (yes+no)//2
        if checkBFS(Y, X, grid, mid, sqY, sqX) == True:
            yes = mid
        else:
            no = mid

    return yes


def main():
    Y, X, K = map(int, input().split())
    grid = [[0] * X for _ in range(Y)]
    for i in range(K):
        y, x = map(int, input().split())
        grid[y-1][x-1] = i+1
    sY, sX, eY, eX = map(int, input().split())
    print(solve(Y, X, K, grid, (sY-1, eY-1), (sX-1, eX-1)))


main()
