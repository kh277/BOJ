# 백준 17370

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
dx1 = (0, 2, -2)
dy1 = (2, -1, -1)
dx2 = (2, 0, -2)
dy2 = (1, -2, 1)


def DFS(N, depth, curP, visited, before):
    curX, curY = curP
    result = 0

    for i in range(3):
        # 다음 이동 좌표
        if depth % 2 == 0:
            nextX = curX + dx1[i]
            nextY = curY + dy1[i]
        else:
            nextX = curX + dx2[i]
            nextY = curY + dy2[i]
        nextP = (nextX, nextY)

        # N번 이동한 뒤 방문한 정점을 재방문했고, 바로 직전에 이동한 경로로 되돌아가지 않은 경우
        if depth == N:
            if visited[nextY][nextX] == 1 and before != nextP:
                return 1
            else:
                return 0

        # N번 미만으로 이동했고, 다음 정점을 아직 방문하지 않은 경우
        elif visited[nextY][nextX] == 0:
            visited[nextY][nextX] = 1
            result += DFS(N, depth+1, nextP, visited, curP)
            visited[nextY][nextX] = 0

    return result


def main():
    N = int(input())
    visited = [[0 for _ in range(100)] for _ in range(100)]
    visited[50][50] = 1
    print(DFS(N, 0, (50, 50), visited, (50, 50)))


main()
