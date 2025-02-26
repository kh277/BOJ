# 백준 1917

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def checkAllZero(A):
    for i in A:
        if i != 0:
            return False

    return True


# 0으로만 이루어진 가로, 세로 모서리 제거
def deleteBlank(grid):
    canLeftX = [0, len(grid[0])]
    canLeftY = [0, len(grid)]
    
    # 위쪽 가로줄 제거
    for y in range(len(grid)):
        if checkAllZero(grid[y]) == True:
            canLeftY[0] += 1
        else:
            break

    # 아래쪽 가로줄 제거
    for y in range(len(grid)-1, -1, -1):
        if checkAllZero(grid[y]) == True:
            canLeftY[1] -= 1
        else:
            break

    # 앞쪽 가로줄 제거
    for x in range(len(grid[0])):
        if checkAllZero([i[x] for i in grid]) == True:
            canLeftX[0] += 1
        else:
            break

    # 뒤쪽 가로줄 제거
    for x in range(len(grid[0])-1, -1, -1):
        if checkAllZero([i[x] for i in grid]) == True:
            canLeftX[1] -= 1
        else:
            break

    return [i[canLeftX[0]:canLeftX[1]] for i in grid[canLeftY[0]:canLeftY[1]]]


# grid 배열 90도 회전
def rotateGrid(grid):
    result = [[0 for _ in range(len(grid))] for _ in range(len(grid[0]))]

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            result[x][y] = grid[y][x]

    return result


def solve(grid):
    # 배열의 가장자리 0 제거
    stripGrid = deleteBlank(grid)
    
    # 가로가 더 작아지도록 배열 회전
    if len(stripGrid) > len(stripGrid[0]):
        stripGrid = rotateGrid(stripGrid)

    # 이진수 형태로 변환
    binNum = ''.join(''.join(str(num) for num in row) for row in stripGrid)

    diagramSet = {'100011111000', '100011110100', '100011110010', '100011110001',
                '010011111000', '010011110100', '010011110010', '010011110001',
                '001011111000', '001011110100', '001011110010', '001011110001',
                '000111111000', '000111110100', '000111110010', '000111110001',
                '110001110100', '001111100010', '001011100011', '010001111100',
                '110001110010', '001111100100', '010011100011', '001001111100',
                '110001110001', '001111101000', '000101111100', '100011100011',
                '110001100011', '001101101100', '1110000111', '0011111100'}

    # set에 포함 유무 체크
    if binNum in diagramSet:
        return 'yes'
    
    return 'no'


def main():
    for _ in range(3):
        grid = []
        for _ in range(6):
            grid.append(list(map(int, input().split())))
        print(solve(grid))


main()
