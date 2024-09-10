# 백준 1633

'''
DP[i][w][b] = i번째 사람을 정할 때, 백팀에 사람이 w명, 흑팀에 사람이 b명 있을 때 최대값.
'''

import sys
import heapq

TEAM_MAX = 15


def solve(N: int, people: list) -> int:
    DP = [[[0 for _ in range(TEAM_MAX+2)] for _ in range(TEAM_MAX+2)] for _ in range(N+1)]

    for i in range(N):
        cur_white, cur_black = people[i]     # 현재 사람의 백팀, 흑팀 점수

        for white in range(TEAM_MAX+1):
            for black in range(TEAM_MAX+1):
                # i번째 인덱스 사람을 백팀에 넣음
                DP[i+1][white+1][black] = max(DP[i+1][white+1][black], DP[i][white][black]+cur_white)
                
                # i번째 인덱스 사람을 흑팀에 넣음
                DP[i+1][white][black+1] = max(DP[i+1][white][black+1], DP[i][white][black]+cur_black)
                
                # i번째 인덱스 사람을 팀에 넣지 않음
                DP[i+1][white][black] = max(DP[i+1][white][black], DP[i][white][black])

    return DP[N][TEAM_MAX][TEAM_MAX]


def main():
    people = []
    for i in sys.stdin:
        people.append([int(x) for x in i.split()])
    
    print(solve(len(people), people))
    

main()