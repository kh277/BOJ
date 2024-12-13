# 백준 1082

'''
DP[i][j] = j원을 사용해 만들 수 있는 i+1자릿수의 가장 큰 번호
'''

import sys

input = sys.stdin.readline

def solve():
    # 숫자의 가격이 오름차순이 되도록 설정
    before = price[-1]
    for i in range(N-1, -1, -1):
        if before < price[i]:
            price[i] = before
        else:
            before = price[i]

    DP = [[-1 for _ in range(M+1)] for _ in range(M//price[0])]
    
    # 1자리 수에 대해 처리
    if M//price[0] >= 1:
        for curPrice in range(N):
            for j in range(price[curPrice], M+1):
                DP[0][j] = curPrice

    # 2자리 수 이상에 대해 처리
    for curDigit in range(1, M//price[0]):
        for curMoney in range(1, M+1):
            for gap in range(curMoney):
                if DP[0][gap] != -1 and DP[curDigit-1][curMoney-gap] != -1:
                    DP[curDigit][curMoney] = max(DP[curDigit][curMoney],
                        int(str(DP[0][gap]) + str(DP[curDigit-1][curMoney-gap])),
                        int(str(DP[curDigit-1][curMoney-gap])+str(DP[0][gap])))

    return max([i[-1] for i in DP])


# main 함수 ----------
N = int(input())
price = list(map(int, input().split()))
M = int(input())

print(solve())
