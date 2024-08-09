# 백준 9465

'''
LIS 문제와 동일하다.
왼쪽 열에서 오른쪽 열로 DP를 진행해 나간다.
이전 값들 중 최대값에 현재 값을 더해서 DP 테이블에 저장한다.
'''

import sys

input = sys.stdin.readline


def solve(N: int, graph: list) -> int:
    # DP 테이블의 구조는 테스트 케이스의 입력과 동일함
    DP = [[0 for _ in range(N)] for _ in range(2)]

    # DP 초기값 설정
    DP[0][0] = graph[0][0]
    DP[1][0] = graph[1][0]
    
    if N < 2:
        return max(DP[0][0], DP[1][0])
    
    DP[0][1] = DP[1][0] + graph[0][1]
    DP[1][1] = DP[0][0] + graph[1][1]

    if N < 3:
        return max(DP[0][1], DP[1][1])
    
    for i in range(2, N):
        DP[0][i] = max(DP[1][i-1], DP[1][i-2]) + graph[0][i]
        DP[1][i] = max(DP[0][i-1], DP[0][i-2]) + graph[1][i]
        
    return max(DP[0][N-1], DP[1][N-1])


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        graph = []
        graph.append(list(map(int, input().split())))
        graph.append(list(map(int, input().split())))
    
        print(solve(N, graph))
    

main()