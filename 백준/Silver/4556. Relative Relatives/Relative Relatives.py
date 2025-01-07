# 백준 4556

'''
T개의 데이터 세트에 대해 아래 문제의 답을 구해야 한다.
Ted는 100살이고, (부모) (자식) (자식을 낳았을 때 부모의 나이) 순서로 자손 목록이 X개 주어진다.
이 때, Ted의 자손 목록을 나이 내림차순, 나이가 같을 경우 이름 사전순으로 출력해야 한다.

딕셔너리로 부모-자식 관계를 저장하고, BFS로 후손을 탐색하면 된다.
'''

import sys
from collections import deque

input = sys.stdin.readline


def solve():
    dic = dict()

    for asc, des, gap in desc:
        if asc in dic:
            dic[asc].append((des, int(gap)))
        else:
            dic[asc] = [(des, int(gap))]

    q = deque()
    q.append(['Ted', 100])
    result = []
    
    while q:
        curData = q.popleft()

        if curData[0] in dic:
            for nextData in dic[curData[0]]:
                q.append([nextData[0], curData[1]-int(nextData[1])])
                result.append([nextData[0], curData[1]-int(nextData[1])])

    return result


# main 함수 ----------
T = int(input())
for i in range(1, T+1):
    print('DATASET', i)
    desc = []
    X = int(input())
    for _ in range(X):
        desc.append(list(map(str, input().rstrip().split())))

    for i in sorted(solve(), key= lambda x: (-x[1], x[0])):
        print(*i)