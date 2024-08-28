# 백준 31404


import sys

input = sys.stdin.readline


def nextMove(curY: int, curX: int, curWay: int, rotate: int) -> list:
    nextWay = (curWay + rotate) % 4
    
    moveY = [-1, 0, 1, 0]
    moveX = [0, 1, 0, -1]

    return [curY+moveY[nextWay], curX+moveX[nextWay], nextWay]


def solve(H: int, W: int, start: list, A: list, B: list) -> int:
    dust = [[1 for _ in range(W)] for _ in range(H)]

    curY, curX, curWay = start
    move = 0
    move_stack = [0, set()]
    while True:
        nextY, nextX, nextWay = None, None, None

        # 탈출 조건1 - 영역을 벗어난 경우
        if not (0 <= curY < H and 0 <= curX < W):
            return move+1
        
        # 탈출 조건2 - 더 이상 먼지를 제거할 수 없는 경우
        if (curY, curX, curWay) in move_stack[1]:
            return move+1

        # 먼지가 있는 경우
        if dust[curY][curX] == 1:
            dust[curY][curX] = 0
            nextY, nextX, nextWay = nextMove(curY, curX, curWay, A[curY][curX])
            move += move_stack[0]
            move_stack = [0, set()]

        # 먼지가 없는 경우
        else:
            nextY, nextX, nextWay = nextMove(curY, curX, curWay, B[curY][curX])
            move_stack[1].add((curY, curX, curWay))

        # 한 칸 이동
        curY, curX, curWay = nextY, nextX, nextWay
        move_stack[0] += 1


def main():
    H, W = map(int, input().split())
    R, C, D = map(int, input().split())

    A = []
    for _ in range(H):
        A.append(list(map(int, input().rstrip())))
    
    B = []
    for _ in range(H):
        B.append(list(map(int, input().rstrip())))
    
    print(solve(H, W, [R, C, D], A, B))


main()