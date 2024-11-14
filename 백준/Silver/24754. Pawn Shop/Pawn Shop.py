# 백준 21748

import sys
from collections import deque

input = sys.stdin.readline


def solve():
    # 원본 배열의 값과 인덱스를 딕셔너리에 저장
    dic = dict()
    for i in range(N):
        if origin[i] in dic:
            dic[origin[i]].append(i)
        else:
            dic[origin[i]] = deque([i])

    # 재배치된 배열에서 분할할 수 있는지 탐색
    result = []
    maxData = 0
    for i in range(N):
        result.append(rearr[i])
        maxData = max(maxData, dic[rearr[i]][0])
        dic[rearr[i]].popleft()
        if maxData == i:
            result.append('#')
    
    # 마지막에 붙은 '#' 제거
    result.pop()
    return result


# main 함수 ----------
N = int(input())
origin = list(map(int, input().split()))
rearr = list(map(int, input().split()))

print(*solve())