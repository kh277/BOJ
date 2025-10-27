# 백준 16432

'''
하루에 만드는 떡의 종류가 최대 9개까지이므로, 호랑이에게 줬던 떡을 누적해서 저장해도 된다.
DP[i][j] = i일에 떡 j를 호랑이에게 줄 수 있는지 여부
이 DP는 i-1의 데이터만 접근하므로 일차원 DP로 간략화 가능함.
'''

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


# 어제 먹었던 떡과 다른 종류의 떡을 줄 수 있다면 그 떡의 번호 리턴
def findPrev(curC, prevDP):
    for prevC in range(1, 10):
        if curC != prevC and len(prevDP[prevC]) != 0:
            return prevC
    return -1


def solve(N, cake):
    prevDP = [array('I') for _ in range(10)]
    for i in cake[0]:
        prevDP[i] = array('I', [i])

    for day in range(1, N):
        DP = [array('I') for _ in range(10)]
        # 오늘 줄 수 있는 떡을 체크
        canGive = False
        for curC in cake[day]:
            prevC = findPrev(curC, prevDP)
            if prevC != -1:
                DP[curC] = prevDP[prevC][:]
                DP[curC].append(curC)
                canGive = True

        # 오늘 줄 수 있는 떡이 없다면
        if canGive == False:
            return [-1]
        prevDP = DP

    # 떡을 줄 방법 리턴
    for i in range(1, 10):
        if len(prevDP[i]) != 0:
            return prevDP[i]

    return [-1]


def main():
    N = int(input())
    cake = []
    for _ in range(N):
        _, *L = map(int, input().split())
        cake.append(L)

    for i in solve(N, cake):
        print(i)


main()
