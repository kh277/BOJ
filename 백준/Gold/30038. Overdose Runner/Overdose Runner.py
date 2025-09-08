# 백준 30038

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
delta = {'u' : (-1, 0), 'd': (1, 0), 'l': (0, -1), 'r': (0, 1)}


class Wall:
    symbol = '*'
    def __init__(self):
        self.pos = None

    def setPos(self, pos):
        self.pos = pos


class Goal:
    symbol = 'g'
    def __init__(self):
        self.pos = None

    def setPos(self, pos):
        self.pos = pos

    def getPos(self):
        return self.pos


class Monster:
    symbol = 'm'
    def __init__(self, HP, DEF, EXP):
        self.pos = None
        self.HP = HP
        self.DEF = DEF
        self.EXP = EXP

    def setPos(self, pos):
        self.pos = pos

    def getHP(self):
        return self.HP

    def getEXP(self):
        return self.EXP

    def getDamage(self, attackDamage):
        self.HP = max(0, self.HP - max((0, attackDamage - self.DEF)))


class Player:
    symbol = 'p'
    def __init__(self):
        self.pos = None
        self.ATK = 5
        self.ATK_RAN = 1
        self.MOVE = 1
        self.needEXP = 10
        self.curEXP = 0
        self.LV = 1
        self.drugCount = 0
        self.overDose = 0

    def levelUp(self):
        while self.curEXP >= self.needEXP:
            self.ATK += self.LV
            self.ATK_RAN += 1
            self.curEXP -= self.needEXP
            self.needEXP += 10
            self.LV += 1

    def setPos(self, pos):
        self.pos = pos

    def getPos(self):
        return self.pos

    # Clear 후 정보 출력
    def getStatus(self):
        return [self.LV, self.curEXP]

    # Teleport 시도
    def tryTeleport(self, grid, moveCommand):
        nextX = self.pos[1] + delta[moveCommand][1]*self.MOVE
        nextY = self.pos[0] + delta[moveCommand][0]*self.MOVE
        if grid.Teleport([nextY, nextX]) == True:
            self.pos = [nextY, nextX]
            self.overDose = max(0, self.overDose - 1)
            return True
        return False

    # Wait 시도
    def tryWait(self):
        self.overDose = max(0, self.overDose - 1)
        return True

    # Attack 시도
    def tryAttack(self, grid, attackCommand):
        # overdose 상태일 경우 행동 불가
        if self.overDose > 0:
            return False

        curY, curX = self.pos
        canMove = self.ATK_RAN
        getEXP = 0
        while canMove:
            nextY = curY + delta[attackCommand][0]
            nextX = curX + delta[attackCommand][1]
            nextData = grid.getData([nextY, nextX])

            # 다음 좌표에 장애물이 있는 경우
            if type(nextData) in {Wall, bool}:
                break
            # 다음 좌표에 몬스터가 있는 경우
            elif type(nextData) == Monster:
                nextData.getDamage(self.ATK)
                if nextData.getHP() == 0:
                    getEXP += nextData.getEXP()
                    grid.deleteData([nextY, nextX])
            curX = nextX
            curY = nextY
            canMove -= 1

        self.curEXP += getEXP
        self.levelUp()
        return True

    # Dose 시도
    def tryDose(self, delta):
        # overdose 상태일 경우 행동 불가
        if self.overDose > 0:
            return False
        self.MOVE = max(0, self.MOVE + delta)
        self.drugCount += 1

        if self.drugCount == 5:
            self.drugCount = 0
            self.overDose += 10
        return True

    # Clear 시도
    def tryClear(self, gridData):
        # overdose 상태일 경우 행동 불가
        if self.overDose == 0 and type(gridData.getData(self.pos)) == Goal:
            return True
        return False


class Grid:
    def __init__(self, X, Y, initGrid, player, monster, goal):
        self.X = X
        self.Y = Y
        self.grid = [[None for _ in range(self.X)] for _ in range(self.Y)]
        self.player = player
        self.goal = goal
        self.monster = monster
        self.leftMonster = 0
        self.gridSetting(initGrid)

    # 초기 grid에 goal, monster 객체 배치
    def gridSetting(self, initGrid):
        for y in range(self.Y):
            for x in range(self.X):
                if initGrid[y][x] == 'p':
                    self.player.setPos([y, x])
                elif initGrid[y][x] == 'm':
                    curM = self.monster[self.leftMonster]
                    curM.setPos([y, x])
                    self.grid[y][x] = curM
                    self.leftMonster += 1
                elif initGrid[y][x] == 'g':
                    self.goal.setPos([y, x])
                    self.grid[y][x] = self.goal
                elif initGrid[y][x] == '*':
                    wall = Wall()
                    wall.setPos([y, x])
                    self.grid[y][x] = wall

    # pos 위치에 어떤 객체가 있는지 반환
    def getData(self, pos):
        if 0 <= pos[1] < self.X and 0 <= pos[0] < self.Y:
            return self.grid[pos[0]][pos[1]]
        return False

    # pos 위치의 객체 삭제
    def deleteData(self, pos):
        self.grid[pos[0]][pos[1]] = None

    # Player 행동 : 이동 범위 체크 후 endPos로 이동
    def Teleport(self, endPos):
        nextY, nextX = endPos
        if 0 <= endPos[1] < self.X and 0 <= endPos[0] < self.Y:
            if type(self.grid[nextY][nextX]) not in {Wall, Monster}:
                return True

    # 게임 종료 후 행동 : 맵에 존재하는 몬스터 체크
    def getTotalMonster(self):
        monsters = []
        for y in range(self.Y):
            for x in range(self.X):
                if type(self.grid[y][x]) == Monster:
                    monsters.append(self.grid[y][x].getHP())
        return monsters

    # 게임 종료 후 행동 : 맵 출력
    def printData(self, player):
        playerY, playerX = player.getPos()
        for y in range(self.Y):
            for x in range(self.X):
                curT = self.grid[y][x]
                # 플레이어는 평소에 grid에 표시하지 않다가 printData를 할 때만 표시
                if y == playerY and x == playerX:
                    print("p", end="")
                elif curT == None:
                    print(".", end="")
                else:
                    print(curT.symbol, end="")
            print()


def main():
    N, M = map(int, input().split())
    initGrid = []
    for _ in range(N):
        initGrid.append(list(input().decode().strip()))

    K = int(input())
    mHP = list(map(int, input().split()))
    mDEF = list(map(int, input().split()))
    mEXP = list(map(int, input().split()))

    # 객체 생성
    player = Player()
    goal = Goal()
    monster = []
    for i in range(K):
        monster.append(Monster(mHP[i], mDEF[i], mEXP[i]))
    gridData = Grid(M, N, initGrid, player, monster, goal)

    # 커맨드 수행
    S = int(input())
    useMovement = 0
    for command in list(input().decode().split()):
        # 텔레포트
        if command in {'u', 'd', 'l', 'r'}:
            if player.tryTeleport(gridData, command) == True:
                useMovement += 1
        # 대기
        elif command == 'w':
            if player.tryWait() == True:
                useMovement += 1
        # 공격
        elif command in {'au', 'ad', 'al', 'ar'}:
            if player.tryAttack(gridData, command[1:]) == True:
                useMovement += 3
        # 약 먹기
        elif command == 'du':
            if player.tryDose(1) == True:
                useMovement += 2
        elif command == 'dd':
            if player.tryDose(-1) == True:
                useMovement += 2
        # 클리어
        elif command == 'c':
            if player.tryClear(gridData) == True:
                break

    # 게임 클리어 후 화면 출력
    print(*player.getStatus())
    print(useMovement)
    gridData.printData(player)
    leftMonster = gridData.getTotalMonster()
    if len(leftMonster) > 0:
        print(*leftMonster)


main()
