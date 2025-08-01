# 백준 7531

'''
N*M 크기의 격자에서 사전순으로 제일 앞서는 나이트투어를 출력하면 된다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
dx = (-1, 1, -2, 2, -2, 2, -1, 1)
dy = (-2, -2, -1, -1, 1, 1, 2, 2)
result = []


def DFS(Y, X, curP, grid, moveCount):
    curY, curX = curP

    # 성공적으로 탐색을 끝낸 경우
    if moveCount == Y*X:
        alpha = [chr(ord('A')+i) for i in range(Y)]
        temp = [0 for _ in range(X*Y)]
        for y in range(Y):
            for x in range(X):
                temp[grid[y][x]] = alpha[y] + str(x+1)
        result.append(''.join(map(str, temp)))
        return True

    # 다음 분기 탐색
    for i in range(8):
        nextX = curX + dx[i]
        nextY = curY + dy[i]

        if 0 <= nextX < X and 0 <= nextY < Y and grid[nextY][nextX] == -1:
            grid[nextY][nextX] = moveCount
            if DFS(Y, X, (nextY, nextX), grid, moveCount+1) == True:
                return True
            grid[nextY][nextX] = -1
    
    return False


def solve(Y, X):
    # 백트래킹으로 나이트투어 진행
    grid = [[-1] * X for _ in range(Y)]
    grid[0][0] = 0

    DFS(Y, X, (0, 0), grid, 1)
    if len(result) == 0:
        return 'impossible'
    return result[0]


def main():
    global result
    T = int(input())
    for i in range(T):
        X, Y = map(int, input().split())
        print(f"Scenario #{i+1}:\n{solve(Y, X)}\n")
        result = []


main()
