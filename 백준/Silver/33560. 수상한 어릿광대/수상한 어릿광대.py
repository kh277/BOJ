# E번

'''
게임 시작 -> 주사위 굴리기 -> 효과 실행 -> 점수 획득 -> 시간 경과
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def calculateTotalScore(score):
    if 35 <= score < 65:
        return 1
    elif 65 <= score < 95:
        return 2
    elif 95 <= score < 125:
        return 3
    elif score >= 125:
        return 4

    return 0


def solve(N, dice):
    result = [0, 0, 0, 0, 0]

    diceIndex = 0       # 주사위를 굴린 횟수
    curTime = 0         # 게임 시작 후 지난 시각
    timeCoef = 4        # 매 턴마다 흐르는 시간
    scoreCoef = 1       # 매 판마다 얻는 점수
    curScore = 0        # 획득한 점수

    while diceIndex < N:
        # 0. 시간 체크
        if curTime > 240:
            result[calculateTotalScore(curScore)] += 1
            curTime = 0
            timeCoef = 4
            scoreCoef = 1
            curScore = 0
            continue

        # 1. 주사위 굴리기
        curDice = dice[diceIndex]

        # 2. 주사위 효과 실행
        if curDice == 1:
            result[calculateTotalScore(curScore)] += 1
            diceIndex += 1
            curTime = 0
            timeCoef = 4
            scoreCoef = 1
            curScore = 0
            continue

        elif curDice == 2:
            if scoreCoef > 1:
                scoreCoef /= 2
            elif scoreCoef == 1:
                timeCoef += 2
        
        elif curDice == 3:
            pass

        elif curDice == 4:
            curTime += 56

        elif curDice == 5:
            if timeCoef > 1:
                timeCoef -= 1

        elif curDice == 6:
            if scoreCoef < 32:
                scoreCoef *= 2

        # 3. 점수 추가
        curScore += scoreCoef
        diceIndex += 1

        # 4. 시간 진행
        curTime += timeCoef

    # 게임 종료 시
    if curTime > 240:
        result[calculateTotalScore(curScore)] += 1

    return result[1:]


def main():
    N = int(input())
    dice = list(map(int, input().split()))
    for i in solve(N, dice):
        print(i)


main()