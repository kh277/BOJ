# 백준 2041

'''
우선 3*3 크기의 배열을 예시로 생각해 보자.
1 2 8
3 7 15
6 16 27 과 같은 배열이 정답이 될 수 있다.
위 배열을 잘 보면,
(0, 0) -> (0, 1) : 차이 1
(0, 0) -> (1, 0) : 차이 2
(1, 0) -> (2, 0) : 차이 3
(1, 0) -> (1, 1) : 차이 4
(0, 1) -> (1, 1) : 차이 5
(0, 1) -> (0, 2) : 차이 6
(0, 2) -> (1, 2) : 차이 7
(1, 1) -> (1, 2) : 차이 8
...
와 같이 지그재그 대각선 순서로 수를 채워넣으면 정답이 되는 배열을 만들 수 있다.
'''

import sys

input = sys.stdin.readline


def solve():
    grid = [[0 for _ in range(2*M-1)] for _ in range(2*N-1)]

    # 1. grid에 인접한 수의 차이 계산
    # curDiagonal : 현재 탐색하고자 하는 대각선의 x, y 인덱스의 합
    index = 1
    for curDiagonal in range(1, 2*(N+M-2)+1, 2):
        startRangeX = max(0, curDiagonal-2*N+2)
        endRangeX = min(curDiagonal, 2*M-2)

        # 좌하단->우상단 대각선
        if (curDiagonal + 3) % 4 == 2:
            for curX in range(startRangeX, endRangeX+1):
                curY = curDiagonal - curX
                grid[curY][curX] = index
                index += 1

        # 우상단->좌하단 대각선
        else:
            for curX in range(endRangeX, startRangeX-1, -1):
                curY = curDiagonal - curX
                grid[curY][curX] = index
                index += 1

    # 2. grid에 저장된 인접한 수끼리 덧셈 연산
    grid[0][0] = 1
    for curX in range(0, 2*M-3, 2):
        grid[0][curX+2] = grid[0][curX] + grid[0][curX+1]
    for curY in range(0, 2*N-3, 2):
        grid[curY+2][0] = grid[curY][0] + grid[curY+1][0]
    
    for curY in range(2, 2*N-1, 2):
        for curX in range(0, 2*M-3, 2):
            grid[curY][curX+2] = grid[curY][curX] + grid[curY][curX+1]

    # 3. grid에 저장된 수 추출
    result = [[0 for _ in range(M)] for _ in range(N)]
    for curY in range(N):
        for curX in range(M):
            result[curY][curX] = grid[curY*2][curX*2]

    return result


# main 함수 ----------
N, M = map(int, input().split())
for i in solve():
    print(*i)