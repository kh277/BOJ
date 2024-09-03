# 백준 1577

'''
4 4
4
1 1 2 1
2 1 3 1
2 2 2 3
1 3 2 3
-> 22
'''

import sys

input = sys.stdin.readline


def check_road(x: int, y: int, road: list) -> bool:
    for i in range(len(road)):
        if [x, y] == [road[i][2], road[i][3]]:
            return [True, road[i]]
        
    return [False, None] 


def solve(N: int, M: int, K: int, road: list) -> int:
    DP = [[0 for _ in range(M+1)] for _ in range(N+1)]
    
    # 공사중인 거리의 x, y좌표 증가순 정렬
    for i in range(K):
        a, b, c, d = road[i]
        if a == c and b > d:
            road[i] = (road[i][0], road[i][3], road[i][2], road[i][1])
        elif b == d and a > c:
            road[i] = (road[i][2], road[i][1], road[i][0], road[i][3])
        else:
            road[i] = (road[i][0], road[i][1], road[i][2], road[i][3])
    
    # road를 set로 변환
    road = set(road)

    # 이후 좌표에 대해 탐색 진행
    for x in range(N+1):
        for y in range(M+1):
            # 초기값
            if x == 0 and y == 0:
                DP[0][0] = 1
            # 현재 좌표가 y축 위에 있을 경우
            elif x == 0:
                if (0, y-1, 0, y) in road:
                    DP[x][y] = 0
                else:
                    DP[x][y] = DP[x][y-1]
            # 현재 좌표가 x축 위에 있을 경우
            elif y == 0:
                if (x-1, 0, x, 0) in road:
                    DP[x][y] = 0
                else:
                    DP[x][y] = DP[x-1][y]
            else:
                # y가 0이 아니거나, (x-1,y)~(x,y)가 세트에 없는 경우 -> x-1 간선 추가
                if (x-1, y, x, y) not in road:
                    DP[x][y] += DP[x-1][y]
                
                # x가 0이 아니거나, (x,y-1)~(x,y)가 세트에 없는 경우 -> y-1 간선 추가
                if (x, y-1, x, y) not in road:
                    DP[x][y] += DP[x][y-1]

    return DP[N][M]


def main():
    N, M = map(int, input().split())
    K = int(input())
    
    road = []
    for _ in range(K):
        road.append(list(map(int, input().split())))
        
    print(solve(N, M, K, road))


main()