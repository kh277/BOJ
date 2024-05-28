# 백준 2578

import sys

input = sys.stdin.readline


def check_bingo(num: list) -> int:
    bingo = 0

    # 빙고 확인
    for i in range(5):
        bingoX = 0
        bingoY = 0
        
        # 가로줄 빙고 확인
        for j in range(5):
            if num[i][j] == 0:
                bingoX += 1
            if num[j][i] == 0:
                bingoY += 1

        if bingoX == 5:
            bingo += 1
        if bingoY == 5:
            bingo += 1
        
    # 대각선 빙고 확인
    bingoA = 0
    bingoB = 0
    for i in range(5):
        if num[i][i] == 0:
            bingoA += 1
            
        if num[i][4-i] == 0:
            bingoB += 1
            
    if bingoA == 5:
        bingo += 1
    if bingoB == 5:
        bingo += 1
    
    return bingo


def solve(num: list, req: list) -> int:
    count = 0

    while True:
        
        # 숫자의 위치 확인
        for y in range(5):
            for x in range(5):
                if num[y][x] == req[count]:
                    num[y][x] = 0
                    count += 1

                    # 종료 조건
                    if check_bingo(num) >= 3:
                        return count


def main():
    num = []
    req = []

    for i in range(5):
        num.append(list(map(int, input().split())))
    
    for i in range(5):
        req.append(list(map(int, input().split())))

    print(solve(num, [x for y in req for x in y]))


main()
