# 백준 2096

'''
1149번 문제와 거의 비슷하다.
다만 메모리 제한이 4MB이기 때문에 리스트 사용을 최소화해야 한다.
'''

import sys

input = sys.stdin.readline

def solve(N: int, num: list) -> list:
    result = [None, None]
    DP = [[0, 0, 0] for _ in range(N)]
    DP[0] = [num[0][0], num[0][1], num[0][2]]

    for i in range(1, N):
        DP[i][0] = num[i][0] + max(DP[i-1][0], DP[i-1][1])
        DP[i][1] = num[i][1] + max(DP[i-1][0], DP[i-1][1], DP[i-1][2])
        DP[i][2] = num[i][2] + max(DP[i-1][1], DP[i-1][2])
    
    result[0] = max(DP[N-1])

    for i in range(1, N):
        DP[i][0] = num[i][0] + min(DP[i-1][0], DP[i-1][1])
        DP[i][1] = num[i][1] + min(DP[i-1][0], DP[i-1][1], DP[i-1][2])
        DP[i][2] = num[i][2] + min(DP[i-1][1], DP[i-1][2])

    result[1] = min(DP[N-1])

    return result


def main():
    N = int(input())
    
    num = []
    for _ in range(N):
        num.append(list(map(int, input().split())))
    
    print(*solve(N, num))


main()