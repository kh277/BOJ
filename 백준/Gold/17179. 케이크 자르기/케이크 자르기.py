# 백준 17179

'''
결정 문제 : 가장 작은 조각의 길이가 x가 되도록 잘랐을 때, 나오는 조각이 Q_i개 이상인가? 

롤 케이크의 마지막 끝 부분도 자른다고 생각해야 하므로
자를 지점에 L을 추가하고, split 개수도 1 증가시켜서 계산해야 한다.
'''


import sys

input = sys.stdin.readline


def check(x: int, split: int) -> bool:
    before = 0      # 이전에 잘린 위치
    piece = 0       # 나온 조각의 수

    for i in range(M+1):
        if cutPoint[i] - before >= x:
            before = cutPoint[i]
            piece += 1
    
    return True if piece >= split else False


def solve(split: int) -> int:
    start = 0
    end = L

    # 이분 탐색
    while end > start+1:
        mid = (start+end)//2

        # 결정 문제 조건 확인
        if check(mid, split):
            start = mid
        else:
            end = mid
    
    return end if check(end, split) else start


# main 함수 ----------
N, M, L = map(int, input().split())

cutPoint = []
for _ in range(M):
    cutPoint.append(int(input()))
cutPoint.append(L)      # 거리를 계산해야 하므로 마지막 지점도 포함

for _ in range(N):
    split = int(input())
    print(solve(split+1))       # 마지막 지점도 잘라야 하므로 split+1
