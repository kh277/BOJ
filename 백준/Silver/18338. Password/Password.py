# 백준 18338

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
move = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}


def DFS(pattern, curV, visited, depth):
    # 종료조건
    if depth == len(pattern):
        return 1

    # 이동 처리
    result = 0
    curY, curX = curV
    dy, dx = move[pattern[depth]]
    plus = set()
    for delta in range(1, 3):
        nextX = curX + dx*delta
        nextY = curY + dy*delta
        nextV = (nextY, nextX)
        plus.add(nextV)

        if 0 <= nextX < 3 and 0 <= nextY < 3 and nextV not in visited:
            visited = visited | plus
            result += DFS(pattern, nextV, visited, depth+1)
            visited = visited - plus
        else:
            return result

    return result


def solve(pattern):
    # 모든 시작점에 대해 처리
    result = 0
    for y in range(3):
        for x in range(3):
            start = (y, x)
            result += DFS(pattern, start, {start}, 0)
    return result


def main():
    pattern = list(input().decode().strip())
    print(solve(pattern))


main()
