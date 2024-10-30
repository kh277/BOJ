# 백준 2381

'''
x좌표 차이 + y좌표 차이 가 최대가 되는 두 점을 찾아야 한다.

수식으로 보면
a >= c이고 b >= d일 경우 구하는 값은 a+b - (c+d)가 된다.
이 경우 x좌표+y좌표 값이 가장 큰 점에서 가장 작은 점을 빼면 된다.

a >= c이고 b < d일 경우 구하는 값은 a-b - (c-d)가 된다.
이 경우 x좌표-y좌표 값이 가장 큰 점에서 가장 작은 점을 빼면 된다.

a < c인 경우는 큰 점과 작은 점이 뒤바뀌었을 뿐이므로 고려하지 않아도 된다.
'''

import sys

input = sys.stdin.readline
INF = 2000001

def solve():
    point.sort(key= lambda x: (x[0], x[1]))

    sumList = [INF, -INF]   # [x+y의 최소값, x+y의 최대값]
    for i in range(N):
        sumList[0] = min(sumList[0], point[i][0]+point[i][1])
        sumList[1] = max(sumList[1], point[i][0]+point[i][1])
    
    subList = [INF, -INF]   # [x-y의 최소값, x-y의 최대값]
    for i in range(N):
        subList[0] = min(subList[0], point[i][0]-point[i][1])
        subList[1] = max(subList[1], point[i][0]-point[i][1])
    
    return max(sumList[1]-sumList[0], subList[1]-subList[0])


# main 함수 ----------
N = int(input())
point = []
for _ in range(N):
    point.append(list(map(int, input().split())))

print(solve())