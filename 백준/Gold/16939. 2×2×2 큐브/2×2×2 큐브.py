# 백준 16939

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


# 큐브가 전부 맞춰졌는지 체크
def checkClear(cube):
    for i in range(1, 25, 4):
        if len({cube[i], cube[i+1], cube[i+2], cube[i+3]}) > 1:
            return False
    return True


# cube를 moveType 방향으로 count번 회전 처리
def moveCube(cube, moveType, count):
    # 이동할 인덱스 지정
    index = None
    if moveType == 'U':
        index = [5, 6, 17, 18, 21, 22, 13, 14]
    elif moveType == 'D':
        index = [7, 8, 19, 20, 23, 24, 15, 16]
    elif moveType == 'L':
        index = [1, 3, 5, 7, 9, 11, 24, 22]
    elif moveType == 'R':
        index = [2, 4, 6, 8, 10, 12, 23, 21]
    elif moveType == 'F':
        index = [3, 4, 17, 19, 10, 9, 16, 14]
    elif moveType == 'B':
        index = [1, 2, 18, 20, 12, 11, 15, 13]

    # 이동 처리
    count *= 2
    if count == 2:
        temp1 = cube[index[0]]
        temp2 = cube[index[1]]
        for y in [0, 2, 4]:
            cube[index[y]] = cube[index[(y+2)%8]]
            cube[index[y+1]] = cube[index[(y+3)%8]]
        cube[index[6]] = temp1
        cube[index[7]] = temp2
    elif count == 4:
        for y in [0, 2]:
            cube[index[y]], cube[index[y+4]] = cube[index[y+4]], cube[index[y]]
            cube[index[y+1]], cube[index[y+5]] = cube[index[y+5]], cube[index[y+1]]


def solve(cube):
    # 이미 큐브가 맞춰진 경우
    if checkClear(cube) == True:
        return 0

    move = ['U', 'D', 'L', 'R', 'F', 'B']
    for i in range(len(move)):
        # 정방향 회전
        if i > 0:
            moveCube(cube, move[i-1], 1)
        moveCube(cube, move[i], 1)
        if checkClear(cube) == True:
            return 1

        # 역방향 회전
        moveCube(cube, move[i], 2)
        if checkClear(cube) == True:
            return 1

    return 0


def main():
    cube = [0] + list(map(int, input().split()))
    print(solve(cube))


main()
