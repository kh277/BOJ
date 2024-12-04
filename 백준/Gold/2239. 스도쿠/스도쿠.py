# 백준 2239

import sys

input = sys.stdin.readline
checkRange = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]


# board[y][x]에 num을 넣을 수 있는지를 체크
def promising(y, x, num):
    # y범위 체크
    for i in range(9):
        if board[i][x] == num:
            return False

    # x범위 체크
    for i in range(9):
        if board[y][i] == num:
            return False

    # 사각형 체크
    for i in checkRange[y//3]:
        for j in checkRange[x//3]:
            if board[i][j] == num:
                return False

    return True


def recur(curNum):
    if curNum == 81:
        result.append(board)
        return True

    for i in range(curNum, 81):
        curY = curNum//9
        curX = curNum%9

        # 빈 칸이라면 숫자를 넣을 수 있는지 확인
        if board[curY][curX] == 0:
            for num in range(1, 10):
                if promising(curY, curX, num) == True:
                    board[curY][curX] = num
                    if recur(curNum+1) == True:
                        return True
                    else:
                        board[curY][curX] = 0
            else:
                return False
        else:
            return recur(curNum+1)

    return True


# main 함수 ----------
board = [list(map(int, input().strip())) for _ in range(9)]
result = []
recur(0)
for i in result[0]:
    print("".join(map(str, i)))
