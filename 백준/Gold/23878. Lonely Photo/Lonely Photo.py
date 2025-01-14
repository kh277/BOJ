# 백준 23878

'''
소가 3마리 이상 나오도록 사진을 찍는다.
연속한 3마리 이상의 소 중 HGGGG, HGH와 같이 한 마리의 소가 다른 품종인 경우 "외로운 사진"이라고 한다.
이 때, 외로운 사진의 수를 출력하는 문제이다.
'''

import sys

input = sys.stdin.readline


def solve():
    result = 0

    # 소의 종류가 바뀌는 구간 체크
    changePos = []
    temp = cows[0]
    curCount = 1
    for i in range(1, N):
        if temp == cows[i]:
            curCount += 1
        else:
            changePos.append(curCount)
            temp = cows[i]
            curCount = 1
    changePos.append(curCount)

    # 바뀌는 구간에 대해 개수 체크 
    for i in range(1, len(changePos)-1):
        left = changePos[i-1]
        right = changePos[i+1]

        # ...GGH...인 경우 처리
        if left > 1:
            result += left-1
        
        # ...GHG...인 경우 처리
        if changePos[i] == 1:
            result += left*right

        # ...HGG...인 경우 처리
        if right > 1:
            result += right-1

    # index가 0, N-1인 경우 처리
    if len(changePos) > 1:
        # HGG... 인 경우 처리
        result += changePos[1]-1

        # ...GGH 인 경우 처리
        result += changePos[-2]-1

    return result


# main 함수 ----------
N = int(input())

cows = input().rstrip()
print(solve())
