# 백준 1821

import sys

input = sys.stdin.readline


# 다항식의 결과값이 M인지 확인
def check(coef, cur):
    result = 0
    for i in range(N):
        result += coef[i] * cur[i]

    return True if result == M else False


# 백트래킹을 통해 다항식을 만족하는 순서쌍 도출
def backtrack(cur, used):
    if len(cur) == N:
        if check(coef, cur) == True:
            permut.append(cur)
        return
    
    for i in range(1, N+1):
        if i not in used:
            backtrack(cur+[i], used | {i})
    
    return


def solve():
    global coef, permut
    
    # DP를 통해 크기가 N인 파스칼 삼각형 도출
    DP = [[0 for _ in range(i+1)] for i in range(N)]
    
    # 초기값 설정
    for i in range(N):
        DP[i][i] = 1
        DP[i][0] = 1
    
    for y in range(1, N):
        for x in range(1, y):
            DP[y][x] = DP[y-1][x-1] + DP[y-1][x]
    
    # 마지막 항 계수 추출
    coef = DP[N-1]
    permut = []
    
    # 백트래킹으로 가능한 순서쌍 전부 도출
    backtrack([], set())
    
    # 사전순에서 제일 앞선 순서쌍 반환
    permut.sort()
    return permut[0]


# main 함수 ----------
N, M = map(int, input().split())

print(*solve())