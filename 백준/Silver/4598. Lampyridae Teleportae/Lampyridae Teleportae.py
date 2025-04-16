# 백준 4598

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


# 점 A에서 점 B 방향으로 거리 D만큼 이동했을 때의 좌표
def move(A, B, D):
    dx = B[0]-A[0]
    dy = B[1]-A[1]
    dist = (dx**2+dy**2)**0.5

    # D보다 가까운 지점에 반딧불이가 있는 경우
    if dist <= D:
        return B

    k = D/dist
    return [A[0] + dx*k, A[1] + dy*k]


# 점 A와 점 B의 거리가 1 이하인지 체크 
def checkDistance(A, B):
    if (B[0]-A[0])**2 + (B[1]-A[1])**2 <= 1:
        return True
    else:
        return False


def solve(D, start, point):
    curX = start[0]
    curY = start[1]
    for i in range(len(point)):
        curX, curY = move([curX, curY], point[i], D)
        if checkDistance([curX, curY], point[i]) == True:
            return point[i]

    return []


def main():
    count = 1
    while True:
        D, startX, startY = map(int, input().split())
        if D == 0 and startX == 0 and startY == 0:
            break
        point = []
        while True:
            x, y = map(int, input().split())
            if x == -1 and y == -1:
                break
            point.append([x, y])
        result = solve(D, [startX, startY], point)
        if len(result) == 0:
            print(f"Firefly {count} not caught")
        else:
            print(f"Firefly {count} caught at ({result[0]},{result[1]})")
        count += 1


main()
