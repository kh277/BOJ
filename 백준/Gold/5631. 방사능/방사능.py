# 백준 5631

'''
원의 두 중심점 (ax, ay), (bx, by)과 최대 20만개의 집 좌표가 주어질 때,
원 내부에 있는 좌표의 개수를 구하는 쿼리가 있다.
이 쿼리를 최대 2만번 처리해야 한다.
'''

import sys
import math

input = sys.stdin.readline


def rangeCal(house, ax, ay, bx, by):
    resultA = []
    resultB = []
    
    for x, y in house:
        resultA.append(math.sqrt((x-ax)**2 + (y-ay)**2))
        resultB.append(math.sqrt((x-bx)**2 + (y-by)**2))
        
    return [sorted(resultA), sorted(resultB)]


def solve(rangeList, R):
    result = 0
    for i in range(2):
        houseRange = rangeList[i]
        curR = R[i]
        
        # 이분 탐색
        start = 0
        end = N-1
        
        while end - start > 1:
            mid = (start+end)//2
            
            if houseRange[mid] > curR:
                end = mid
            else:
                start = mid

        if houseRange[end] > curR:
            result += start+1
        else:
            result += end+1
    
    return result


# main 함수 ----------
case = 1
while True:
    N = int(input())
    if N == 0:
        break
    
    print("Case {a}:".format(a=case))
    house = []
    for _ in range(N):
        house.append(list(map(int, input().split())))
        
    ax, ay, bx, by, q = map(int, input().split())
    
    # 두 원의 중심으로부터 떨어진 거리 반환
    rangeListA, rangeListB = rangeCal(house, ax, ay, bx, by)
    for _ in range(q):
        r1, r2 = map(int, input().split())
        # r1, r2일 때 보호 장비를 받지 못하는 집의 수 반환
        print(N - min(N, solve([rangeListA, rangeListB], [r1, r2])))
    
    case += 1