# 백준 13218

'''
입력을 받으면서 DP 테이블에 현재 x값 기준, y값의 최대값과 최소값을 함께 저장한다.
DP[i][0] = x=i일 때, y의 최소값
DP[i][1] = x=i일 때, y의 최대값

i는 최대 3000이므로 O(N^2)으로 풀 수 있다.
'''

import sys

input = sys.stdin.readline


def solve(DP):
    result = 0
    for i in range(0, 2*M):
        for j in range(i+1, 2*M+1):
            if DP[i][0] != INF and DP[i][1] != INF and DP[j][0] != INF and DP[j][1] != INF:
                result = max(result, (DP[i][0] - DP[j][1])**2 + (j-i)**2)
                result = max(result, (DP[j][0] - DP[i][1])**2 + (j-i)**2)
    
    return result


# main 함수 ----------
N = int(input())
M = int(input())
INF = M+1

DP = [[INF, -INF] for _ in range(M*2+1)]
for i in range(N):
    a, b = map(int, input().split())
    DP[a+M][0] = min(DP[a+M][0], b)
    DP[a+M][1] = max(DP[a+M][1], b)

print(solve(DP))