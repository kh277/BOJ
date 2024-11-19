# 백준 3000

import sys

input = sys.stdin.readline


def solve():
    maxValueX = max([point[i][0] for i in range(N)])
    maxValueY = max([point[i][1] for i in range(N)])
    pointX = [[] for _ in range(maxValueX+1)]
    pointY = [[] for _ in range(maxValueY+1)]
    result = 0

    # x=a인 점들의 y좌표 저장, y=b인 점들의 x좌표 저장
    for i in range(N):
        x, y = point[i]
        pointX[x].append(y)
        pointY[y].append(x)
    
    # 모든 점들에 대해 탐색
    for i in range(N):
        x, y = point[i]
        result += (len(pointX[x])-1)*(len(pointY[y])-1)

    return result


# main 함수 ----------
N = int(input())
point = []
for _ in range(N):
    point.append(tuple(map(int, input().split())))
print(solve())