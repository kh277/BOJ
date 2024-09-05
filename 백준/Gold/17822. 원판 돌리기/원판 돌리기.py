# 백준 17822

import sys
from collections import deque

input = sys.stdin.readline


def BFS(N: int, M: int, graph: list, start: list) -> list:
    pointX = [-1, 1, 0, 0]
    pointY = [0, 0, -1, 1]
    start_num = graph[start[0]][start[1]]
    visited = set()
    
    q = deque()
    q.append(start)
    visited.add((start[0], start[1]))
    
    # 큐가 빌 때까지 반복
    while q:
        cur = q.popleft()
        for i in range(4):
            nextX = (cur[1] + pointX[i]) % M
            nextY = cur[0] + pointY[i]
            
            # 시작점과 같은 숫자이고 범위를 벗어나지 않는 경우
            if 0 <= nextX < M and 1 <= nextY < N+1:
                if graph[nextY][nextX] == start_num and (nextY, nextX) not in visited:
                    q.append([nextY, nextX])
                    visited.add((nextY, nextX))
    
    # 같은 수가 2개 이상 붙어있을 경우 0으로 변환
    # 값 수정이 있었으면 True, 없었으면 False 반환
    if len(visited) > 1:
        for y, x in visited:
            graph[y][x] = 0
        return [True, graph]
    else:
        return [False, graph]
    

def solve(N: int, M: int, T: int, circle_num: list, query: list) -> int:
    # T번의 쿼리 처리
    for i in range(len(query)):
        x, d, k = query[i]
        
        # 반시계 방향은 시계 방향으로 전환
        if d == 1:
            k = M - k
        
        # x_i의 배수 원판을 d_i 방향으로 k_i칸만큼 회전
        for j in range(x, N+1, x):
            # for k in range(M):
            circle_num[j] = circle_num[j][M-k:] + circle_num[j][:M-k]
        
        # 인접하면서 수가 같은 것 지우기
        changed = False
        for y in range(1, N+1):
            for x in range(M):
                is_changed = False
                if circle_num[y][x] != 0:
                    is_changed, circle_num = BFS(N, M, circle_num, [y, x])
                if is_changed == True:
                    changed = True

        # 이전 반복에서 수를 지우지 않았다면
        if changed == False:
            avr = [0, 0]        # [남은 숫자 총합, 남은 숫자 개수]
            # 남은 숫자들의 평균 구하기
            for y in range(1, N+1):
                for x in range(M):
                    if circle_num[y][x] != 0:
                        avr[0] += circle_num[y][x]
                        avr[1] += 1
            
            # ZeroDivision Error 처리 (원판에 남은 숫자가 없는데 쿼리가 들어오는 경우)
            if avr[1] == 0:
                fix = 0
            else:
                fix = avr[0] / avr[1]
            
            # 남은 숫자들 +- 1 처리
            for y in range(1, N+1):
                for x in range(M):
                    if circle_num[y][x] != 0:
                        if fix > circle_num[y][x]:
                            circle_num[y][x] += 1
                        elif fix < circle_num[y][x]:
                            circle_num[y][x] -= 1
        
    return sum([sum(x) for x in circle_num])
        

def main():
    N, M, T = map(int, input().split())
    
    # 배수 처리를 해야 하기 때문에 원판을 인덱스 1부터 저장
    circle_num = [[]]
    for _ in range(N):
        circle_num.append(list(map(int, input().split())))
    
    query = []
    for _ in range(T):
        query.append(list(map(int, input().split())))

    print(solve(N, M, T, circle_num, query))


main()