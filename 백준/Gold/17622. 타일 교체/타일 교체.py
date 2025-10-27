# 백준 17622

'''
다음 칸으로 이동할 수 있는지 체크 후 이동하며 시뮬레이션하기.
curFlow, prevFlow의 값 = 위쪽방향(0), 오른쪽방향(1), 아래쪽방향(2), 왼쪽방향(3)
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**4
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


# 현재 타일이 curTile이고 prevFlow 방향에서 흘러 들어온 경우, 흘러 나가는 방향 반환
def getNextFlow(prevFlow, curTile):
    # 위쪽 방향으로 흐르는 경우
    if prevFlow == 0:
        if curTile == 0:
            return 1
        elif curTile == 1:
            return 3
        elif curTile == 4:
            return 0
    # 오른쪽 방향으로 흐르는 경우
    elif prevFlow == 1:
        if curTile == 1:
            return 2
        elif curTile == 3:
            return 0
        elif curTile == 5:
            return 1
    # 아래쪽 방향으로 흐르는 경우
    elif prevFlow == 2:
        if curTile == 2:
            return 1
        elif curTile == 3:
            return 3
        elif curTile == 4:
            return 2
    # 왼쪽 방향으로 흐르는 경우
    else:
        if curTile == 0:
            return 2
        elif curTile == 2:
            return 0
        elif curTile == 5:
            return 3
    return -1


# 현재 grid에서 출발->도착 경로가 만들어지는지 체크
def simulate(N, grid):
    # 출발점 또는 도착점이 이어지지 않은 경우
    if grid[0][0] not in {1, 5} or grid[N-1][N-1] not in {2, 5}:
        return INF

    curX = -1
    curY = 0
    curFlow = 1
    move = 0

    while True:
        # 종료 조건 체크
        if curX == N-1 and curY == N-1:
            return move

        nextX = curX + dx[curFlow]
        nextY = curY + dy[curFlow]

        # 격자 탈출 여부 체크
        if not 0 <= nextX < N or not 0 <= nextY < N:
            return INF
        
        # 다음 칸으로 흐를 수 있는지 체크
        canFlow = False
        nextT = grid[nextY][nextX]
        if curFlow == 0 and nextT in {0, 1, 4}:
            canFlow = True
        elif curFlow == 1 and nextT in {1, 3, 5}:
            canFlow = True
        elif curFlow == 2 and nextT in {2, 3, 4}:
            canFlow = True
        elif curFlow == 3 and nextT in {0, 2, 5}:
            canFlow = True

        if canFlow == False:
            return INF

        # 다음 칸으로 이동
        curX = nextX
        curY = nextY
        curFlow = getNextFlow(curFlow, nextT)
        move += 1


def solve(N, K, grid):
    result = INF
    # 바뀌는 타일이 0개일 경우
    if K == 0:
        result = simulate(N, grid)

    # 바뀌는 타일이 1개일 경우
    else:
        for y in range(N):
            for x in range(N):
                prev = grid[y][x]
                for t in range(6):
                    if prev != t:
                        grid[y][x] = t
                        result = min(result, simulate(N, grid))
                grid[y][x] = prev

    if result == INF:
        return -1
    return result


def main():
    N, K = map(int, input().split())
    grid = []
    for _ in range(N):
        grid.append(list(map(int, input().split())))

    print(solve(N, K, grid))


main()
