# 백준 28457

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


class Player():
    def __init__(self, pos, S):
        self.pos = pos
        self.leftMoney = S


    def getPos(self):
        return self.pos


    def canBuy(self, cost):
        if self.leftMoney >= cost:
            return True
        return False


    def move(self, dist):
        self.pos += dist
        return self.pos


    def calCost(self, cost):
        self.leftMoney += cost


class Board:
    def __init__(self, S, W, G, goldkey, cityData):
        # 객체
        self.player = Player(0, S)
        self.size = len(cityData)
        self.data = cityData
        self.playerPay = W
        # 황금 열쇠
        self.goldkey = goldkey
        self.totalGoldkey = G
        self.curGoldkey = 0
        # 무인도
        self.desertTurn = 0
        # 사회복지기금
        self.accFund = 0
        # 우주여행
        self.isTravel = False


    # 움직일 수 있는지 여부 체크 (0=불가, 1=가능, 2=무인도탈출)
    def canMove(self, diceA, diceB):
        if self.desertTurn > 0:
            if diceA == diceB:
                self.desertTurn = 0
                return 2
            return -1
        return 1


    # 시뮬레이션 1회 시행 (0=파산 1=정상적으로종료)
    def simulation(self, diceA, diceB):
        # 우주여행 처리
        if self.isTravel == True:
            self.player.move(self.size-self.player.getPos())
            self.isTravel = False

        # 이동 처리
        moveType = self.canMove(diceA, diceB)
        if moveType == 2:
            return 1
        elif moveType == 1:
            self.player.move(diceA + diceB)

            # 시작 칸을 지나가는 경우
            if self.player.getPos() >= self.size:
                count = self.player.getPos() // self.size
                self.player.calCost(self.playerPay * count)
                self.player.move(-self.size * count)
        else:
            self.desertTurn -= 1
            return 1
        
        # 이동 후 이벤트 처리
        curCity = self.data[self.player.getPos()]

        # 도시 칸에 방문한 경우
        if curCity[0] == 1 and curCity[2] == 0 and self.player.canBuy(curCity[1]):
            self.player.calCost(-curCity[1])
            curCity[2] = 1

        # 황금열쇠 칸에 방문한 경우
        elif curCity[0] == 2:
            keyType, value = self.goldkey[self.curGoldkey]
            self.curGoldkey += 1
            if self.curGoldkey >= self.totalGoldkey:
                self.curGoldkey = 0
            if keyType == 1:
                self.player.calCost(value)
            elif keyType in {2, 3}:
                if self.player.canBuy(value) == False:
                    return 0
                self.player.calCost(-value)
                if keyType == 3:
                    self.accFund += value
            elif keyType == 4:
                return self.simulation(value, 0)

        # 무인도 칸에 방문한 경우
        elif curCity[0] == 4:
            self.desertTurn += 3

        # 사회복지기금 칸에 방문한 경우
        elif curCity[0] == 5:
            self.player.calCost(self.accFund)
            self.accFund = 0

        # 우주여행 칸에 방문한 경우
        elif curCity[0] == 6:
            self.isTravel = True

        return 1


    def winCheck(self):
        for i in range(self.size):
            if self.data[i][2] == 0:
                return False
        return True


def main():
    N, S, W, G = map(int, input().split())
    goldkey = []
    for _ in range(G):
        goldkey.append(tuple(map(int, input().split())))

    # cityData = [[칸의 종류, 금액, 도시 구매여부], ...]
    # (1=도시, 2=황금열쇠, 3=시작칸, 4=무인도, 5=사회복지기금, 6=우주여행)
    cityData = []
    for _ in range(4*N-8):
        if len(cityData)%(N-1) == 0:
            cityData.append([[3, 0, 1], [4, 0, 1], [5, 0, 1], [6, 0, 1]][len(cityData)//(N-1)])
        a, *b = input().decode().split()
        if a == 'L':
            cityData.append([1, int(b[0]), 0])
        else:
            cityData.append([2, 0, 1])

    marble = Board(S, W, G, goldkey, cityData)

    I = int(input())
    for _ in range(I):
        a, b = map(int, input().split())
        cur = marble.simulation(a, b)
        if cur == 0:
            print('LOSE')
            return
    
    if marble.winCheck() == True:
        print('WIN')
        return
    
    print('LOSE')
    return


main()
