# 백준 14488

'''
1번 학생이 T초 내에 갈 수 있는 범위를 구한다.
2 ~ N번 학생도 갈 수 있는 범위를 구한다.

N개의 선분이 겹치는 곳이 있다면 1을, 없다면 0을 출력한다.
'''

import sys

input = sys.stdin.readline
INF = 10e10


def solve(N: int, T: float, data: list) -> int: 
    start = -INF
    end = INF
    
    for i in range(1, N):
        start = max(start, data[i][0] - data[i][1]*T)
        end = min(end, data[i][0] + data[i][1]*T)
        
        if start > end:
            return 0
    
    return 1


def main():
    N, T = map(float, input().split())
    
    pos = list(map(int, input().split()))
    v = list(map(int, input().split()))
    
    # data에는 [[1번 위치, 1번 속도], [2번 위치, 2번 속도], ...] 순서로 저장
    print(solve(int(N), T, [[pos[i], v[i]] for i in range(int(N))]))
    

main()