# 백준 6614

import io
import math

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


# 시계바늘이 각도 degree를 가리킬 때, 길이가 count인 좌표 반환
def getPos(degree, count, mid):
    result = []     # 좌표평면 기준으로 저장

    # 선의 기울기가 수직 방향에서 0도일 때
    if degree == 0:
        for i in range(count):
            result.append([mid-i, mid])
    elif degree == 180:
        for i in range(count):
            result.append([mid+i, mid])

    # 선의 기울기가 수직 방향에서 90도일 때
    elif degree == 90:
        for i in range(count):
            result.append([mid, mid+i])
    elif degree == 270:
        for i in range(count):
            result.append([mid, mid-i])

    # 선의 기울기가 수직 방향에서 45도 이상일 때
    elif 0 < degree <= 45 or 315 <= degree < 360:
        coefY = 1/math.tan(math.pi * (90-degree) / 180)
        for y in range(count):
            result.append([mid-y, mid+round(coefY*y)])
    elif 135 <= degree <= 225:
        coefY = 1/math.tan(math.pi * (90-degree) / 180)
        for y in range(count):
            result.append([mid+y, mid+round(coefY*-y)])

    # 선의 기울기가 수직 방향에서 45도 이하일 때
    elif 45 < degree < 135:
        coefX = math.tan(math.pi * (90-degree) / 180)
        for x in range(count):
            result.append([mid-round(coefX*x), mid+x])
    else:
        coefX = math.tan(math.pi * (90-degree) / 180)
        for x in range(count):
            result.append([mid-round(coefX*-x), mid-x])

    return result


# 세 정수가 같은지 체크
def sameP(A, B, C):
    if A == B and B == C:
        return True
    return False


# 세 정수가 증가하는지 체크
def increaseP(A, B, C):
    if A+1 == B and B+1 == C:
        return True
    return False


# 좌표들이 주어질 때, o과 | 적절하게 배치
def setPos(grid, point, maxLen):
    grid[point[0][0]][point[0][1]] = 'o'
    for i in range(1, len(point)-1):
        beforeY, beforeX = point[i-1]
        curY, curX = point[i]
        nextY, nextX = point[i+1]

        # 원점까지의 거리가 maxLen을 초과하면 break
        if (curY-25)**2 + (curX-25)**2 > maxLen**2:
            return grid

        # 수평 요소 체크
        if (increaseP(beforeX, curX, nextX) or increaseP(nextX, curX, beforeX)) and sameP(beforeY, curY, nextY):
            grid[curY][curX] = '-'
        # 수직 요소 체크
        elif sameP(beforeX, curX, nextX) and (increaseP(beforeY, curY, nextY) or increaseP(nextY, curY, beforeY)):
            grid[curY][curX] = '|'
        # 대각선(\) 요소 체크
        elif (increaseP(nextX, curX, beforeX) and increaseP(nextY, curY, beforeY)) or \
            (increaseP(beforeX, curX, nextX) and increaseP(beforeY, curY, nextY)):
            grid[curY][curX] = '\\'
        # 대각선(/) 요소 체크
        elif (increaseP(nextX, curX, beforeX) and increaseP(beforeY, curY, nextY)) or \
            (increaseP(beforeX, curX, nextX) and increaseP(nextY, curY, beforeY)):
            grid[curY][curX] = '/'
        else:
            grid[curY][curX] = 'o'

    return grid


def solve(hour, minute):
    maxSize = 51
    mid = maxSize//2

    # 각도 계산
    hourAngle = hour*30 + minute*0.5
    minuteAngle = minute*6
    grid = [[' ' for _ in range(maxSize)] for _ in range(maxSize)]

    # 시침 좌표 처리 및 표시
    hourP = getPos(hourAngle, 25, mid)
    grid = setPos(grid, hourP, 15)

    # 분침 좌표 처리 및 표시
    minuteP = getPos(minuteAngle, 25, mid)
    grid = setPos(grid, minuteP, 21)

    # 테두리 표시
    for i in range(51):
        if i % 10 == 0:
            grid[i][0] = '@'
            grid[i][50] = '@'
            grid[0][i] = '@'
            grid[50][i] = '@'
        else:
            grid[i][0] = 'X'
            grid[i][50] = 'X'
            grid[0][i] = 'X'
            grid[50][i] = 'X'
    
    # 숫자, 시계 중앙 표시
    grid[2][24] = '1'
    grid[2][26] = '2'
    grid[25][2] = '9'
    grid[25][48] = '3'
    grid[48][25] = '6'
    grid[25][25] = '*'

    return [''.join(i) for i in grid]


def main():
    while True:
        t = list(input().decode().rstrip().split(":"))
        if t[0] == 'END':
            break
        
        for i in solve(int(t[0])%12, int(t[1])):
            print(i)
        print()


main()
