# 백준 2983

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
moveWay = {'A': 0, 'B': 1, 'C': 3, 'D': 2}


class Node:
    def __init__(self, x, y, curId):
        self.x = x
        self.y = y
        self.id = curId
        self.nextId = [None, None, None, None]

    def move(self, way):
        return self.nextId[way]


def solve(N, K, point, command):
    data = [None] * N

    # A, D방향 저장
    point.sort(key= lambda x: (x[0], x[1]))
    prevX = -10**10
    for i in range(N):
        curX, curY, curId = point[i]
        cur = Node(curX, curY, curId)
        if prevX == curX:
            cur.nextId[2] = data[point[i-1][2]].id
            data[point[i-1][2]].nextId[0] = curId
        else:
            prevX = curX
        data[curId] = cur

    # B, C방향 저장
    point.sort(key= lambda x: (x[1], x[0]))
    prevY = -10**10
    for i in range(N):
        curX, curY, curId = point[i]
        if prevY == curY:
            data[curId].nextId[3] = data[point[i-1][2]].id
            data[point[i-1][2]].nextId[1] = curId
        else:
            prevY = curY

    # 개구리 이동 처리
    curId = 0
    for i in range(K):
        curNode = data[curId]
        nextVid = curNode.move(moveWay[command[i]])
        if nextVid == None:
            continue

        # 점프 후 식물 삭제 처리
        for i in range(4):
            if curNode.nextId[i] != None:
                nextNode = data[curNode.nextId[i]]
                nextNode.nextId[(i+2)%4] = curNode.nextId[(i+2)%4]

        curId = nextVid

    x = data[curId].x
    y = data[curId].y
    return ((x+y)//2, (y-x)//2)


def main():
    N, K = map(int, input().split())
    command = list(input().decode().strip())
    point = []
    for i in range(N):
        a, b = map(int, input().split())
        point.append((a-b, a+b, i))

    print(*solve(N, K, point, command))


main()
