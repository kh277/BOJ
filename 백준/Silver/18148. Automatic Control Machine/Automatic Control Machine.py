# 백준 18148

import sys

input = sys.stdin.readline
INF = 16


def recur(curIndex, curStatus, depth):
    '''
    startIndex = 현재까지 탐색한 인덱스
    curStatus = 현재까지 검사한 기능의 상태
    depth = 현재 진행한 검사의 수 (재귀 깊이)
    '''
    result = INF
    if bin(curStatus) == '0b' + '1'*N:
        return depth
    elif curIndex == N:
        return INF

    for i in range(curIndex+1, M):
        result = min(result, recur(i, curStatus | data[i], depth+1))
    
    return result


# main 함수 ----------
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    data = []
    for _ in range(M):
        data.append(int(input(), 2))
    cur = recur(-1, 0, 0)
    print(-1 if cur == INF else cur)
