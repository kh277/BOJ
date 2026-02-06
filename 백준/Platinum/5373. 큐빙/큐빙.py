# 백준 5373

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
pos = {'L': (3, 0), 'F': (3, 3), 'R': (3, 6), 'B': (3, 9), 'U': (0, 3), 'D': (6, 3)}


# 좌상단 좌표가 [y0, x0]인 3*3 격자를 angle만큼 회전시키기 
def rotate(cube, y0, x0, angle):
    x1 = x0+1
    x2 = x0+2
    y1 = y0+1
    y2 = y0+2

    # 90도 회전
    if angle == 1:
        cube[y0][x0], cube[y0][x2], cube[y2][x2], cube[y2][x0] = cube[y2][x0], cube[y0][x0], cube[y0][x2], cube[y2][x2]
        cube[y0][x1], cube[y1][x2], cube[y2][x1], cube[y1][x0] = cube[y1][x0], cube[y0][x1], cube[y1][x2], cube[y2][x1]

    # 270도 회전
    else:
        cube[y0][x0], cube[y0][x2], cube[y2][x2], cube[y2][x0] = cube[y0][x2], cube[y2][x2], cube[y2][x0], cube[y0][x0]
        cube[y0][x1], cube[y1][x2], cube[y2][x1], cube[y1][x0] = cube[y1][x2], cube[y2][x1], cube[y1][x0], cube[y0][x1]


# cube에서 command에 따라 줄 밀림 처리
def roll(cube, command):
    dy= None
    dx = None
    angle = 1 if command[1] == '+' else 3
    y0, x0 = pos[command[0]]

    match command:
        # 왼쪽 회전
        case "L+":
            dy = [0, 1, 2, 3, 4, 5, 6, 7, 8, 5, 4, 3]
            dx = [3, 3, 3, 3, 3, 3, 3, 3, 3, 11, 11, 11]
        case "L-":
            dy = [2, 1, 0, 3, 4, 5, 8, 7, 6, 5, 4, 3]
            dx = [3, 3, 3, 11, 11, 11, 3, 3, 3, 3, 3, 3]
        # 오른쪽 회전
        case "R+":
            dy = [2, 1, 0, 3, 4, 5, 8, 7, 6, 5, 4, 3]
            dx = [5, 5, 5, 9, 9, 9, 5, 5, 5, 5, 5, 5]
        case "R-":
            dy = [0, 1, 2, 3, 4, 5, 6, 7, 8, 5, 4, 3]
            dx = [5, 5, 5, 5, 5, 5, 5, 5, 5, 9, 9, 9]
        # 위쪽 회전
        case "U+":
            dy = [3] * 12
            dx = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        case "U-":
            dy = [3] * 12
            dx = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        # 아래쪽 회전
        case "D+":
            dy = [5] * 12
            dx = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        case "D-":
            dy = [5] * 12
            dx = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        # 앞쪽 회전
        case "F+":
            dy = [2, 2, 2, 3, 4, 5, 6, 6, 6, 5, 4, 3]
            dx = [3, 4, 5, 6, 6, 6, 5, 4, 3, 2, 2, 2]
        case "F-":
            dy = [2, 2, 2, 3, 4, 5, 6, 6, 6, 5, 4, 3]
            dx = [5, 4, 3, 2, 2, 2, 3, 4, 5, 6, 6, 6]
        # 뒤쪽 회전
        case "B+":
            dy = [0, 0, 0, 3, 4, 5, 8, 8, 8, 5, 4, 3]
            dx = [5, 4, 3, 0, 0, 0, 3, 4, 5, 8, 8, 8]
        case "B-":
            dy = [0, 0, 0, 3, 4, 5, 8, 8, 8, 5, 4, 3]
            dx = [3, 4, 5, 8, 8, 8, 5, 4, 3, 0, 0, 0]

    # 줄 밀림 처리
    tmp = [cube[dy[9]][dx[9]], cube[dy[10]][dx[10]], cube[dy[11]][dx[11]]]
    for i in range(9, 2, -3):
        cube[dy[i]][dx[i]] = cube[dy[i-3]][dx[i-3]]
        cube[dy[i+1]][dx[i+1]] = cube[dy[i-2]][dx[i-2]]
        cube[dy[i+2]][dx[i+2]] = cube[dy[i-1]][dx[i-1]]
    for i in range(3):
        cube[dy[i]][dx[i]] = tmp[i]

    # 큐브면 회전 처리
    rotate(cube, y0, x0, angle)


def solve(N, Q):
    cube = [[' ', ' ', ' ', 'w', 'w', 'w', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', 'w', 'w', 'w', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', 'w', 'w', 'w', ' ', ' ', ' ', ' ', ' ', ' '],
            ['g', 'g', 'g', 'r', 'r', 'r', 'b', 'b', 'b', 'o', 'o', 'o'],
            ['g', 'g', 'g', 'r', 'r', 'r', 'b', 'b', 'b', 'o', 'o', 'o'],
            ['g', 'g', 'g', 'r', 'r', 'r', 'b', 'b', 'b', 'o', 'o', 'o'],
            [' ', ' ', ' ', 'y', 'y', 'y', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', 'y', 'y', 'y', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', 'y', 'y', 'y', ' ', ' ', ' ', ' ', ' ', ' ']]

    for curQ in Q:
        roll(cube, curQ)

    # 상단 면 추출
    return [''.join(cube[i][3:6]) for i in range(3)]


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        Q = list(input().decode().split())
        for i in solve(N, Q):
            print(i)


main()
