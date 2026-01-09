# 백준 25598

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
dx = [0, 0, -1, 1, 0]
dy = [-1, 1, 0, 0, 0]
moveDict = {'U': 0, 'D': 1, 'L': 2, 'R': 3, 'S': 4}


class Player():
    def __init__(self, sY, sX):
        self.y = sY
        self.x = sX

    def move(self, curY, curX):
        self.y = curY
        self.x = curX


class Zombie():
    def __init__(self, sY, sX, tier, way, speed):
        self.y = sY
        self.x = sX
        self.tier = tier
        self.way = way
        self.speed = speed

    def move(self, curY, curX, way=None):
        self.y = curY
        self.x = curX
        if way != None:
            self.way = way


# 상급 좀비가 다음에 이동할 방향 계산
def getZombieWay(N, grid, curZombie):
    moveWay = [0, 0, 0, 0]
    for i in range(4):
        curY = curZombie.y
        curX = curZombie.x
        while True:
            nextY = curY + dy[i]
            nextX = curX + dx[i]
            if 0 <= nextY < N and 0 <= nextX < N:
                if grid[nextY][nextX] == 1:
                    moveWay[i] += 1
                curY = nextY
                curX = nextX
            else:
                break

    maxW = max(moveWay)
    if moveWay[0] == maxW:
        return 0
    elif moveWay[3] == maxW:
        return 3
    elif moveWay[1] == maxW:
        return 1
    else:
        return 2


def simulation(N, grid, command, player, zombie):
    # 플레이어 이동 처리
    nextY = player.y + dy[moveDict[command]]
    nextX = player.x + dx[moveDict[command]]
    if 0 <= nextY < N and 0 <= nextX < N and grid[nextY][nextX] != 1:
        player.y = nextY
        player.x = nextX

    # 좀비 이동 처리
    for curZombie in zombie:
        curY = curZombie.y
        curX = curZombie.x
        cantMove = False
        for _ in range(curZombie.speed):
            nextY = curY + dy[curZombie.way]
            nextX = curX + dx[curZombie.way]

            if 0 <= nextY < N and 0 <= nextX < N:
                # 벽을 만난 경우
                if grid[nextY][nextX] == 1:
                    if curZombie.tier == 1:
                        grid[nextY][nextX] = 0
                    cantMove = True
                    break
                curY = nextY
                curX = nextX
            else:
                cantMove = True
                break

        # 좀비 위치 저장
        curZombie.y = curY
        curZombie.x = curX

        # 좀비 방향 처리
        if curZombie.tier == 0 and cantMove == True:
            curZombie.way ^= 1
        elif curZombie.tier == 1:
            curZombie.way = getZombieWay(N, grid, curZombie)

    # 플레이어 - 좀비 위치 처리
    for curZombie in zombie:
        if player.x == curZombie.x and player.y == curZombie.y:
            return False

    return True


def main():
    N = int(input())
    grid = [[0] * N for _ in range(N)]
    command = list(input().decode().rstrip())
    pY, pX = map(int, input().split())
    player = Player(pY-1, pX-1)

    W = int(input())
    for _ in range(W):
        y, x = map(int, input().split())
        grid[y-1][x-1] = 1

    Z = int(input())
    zombie = []
    for _ in range(Z):
        y, x, t, w, s = list(input().decode().split())
        zombie.append(Zombie(int(y)-1, int(x)-1, int(t), moveDict[w], min(N+1, int(s))))

    # 쿼리 처리
    D = int(input())
    deadDay = -1
    for i in range(D):
        isAlive = simulation(N, grid, command[i], player, zombie)
        if isAlive == False:
            deadDay = i+1
            break

    if deadDay == -1:
        print(f"ALIVE!")
    else:
        print(f"{deadDay}\nDEAD...")

main()
