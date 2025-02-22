# 백준 3777

'''
DP[i] = [i번째 수의 00 개수, i번째 수의 11 개수, i번째 수의 첫번째 수]
DP[i][0] = DP[i-1][0] + DP[i-1][1]
DP[i][1] = DP[i-1][1] + DP[i-1][0]이고,
i번째 수의 첫 번째 숫자가 0일 경우 DP[i][0]에 1을 더해준다.
1일 경우에는 DP[i][1]에 1을 더해준다.

i번째 수의 첫 번째 수는 0, 1, 0, 1, ... 순으로 반복된다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
DP = [[0, 0, 0] for _ in range(1001)]
calculateCount = 0


def solve(N):
    if N < calculateCount:
        return DP[N][0]
    DP[2] = [1, 0, 1]
    DP[3] = [1, 1, 0]
    
    for i in range(max(4, calculateCount), N+1):
        DP[i] = [DP[i-1][0]+DP[i-1][1], DP[i-1][1]+DP[i-1][0], DP[i-1][2]^1]
        if DP[i-1][2] == 0:
            DP[i][0] += 1
    
    return DP[N][0]


# main 함수 ----------
while True:
    try:
        N = int(input())
        print(solve(N))
        calculateCount = N
    except Exception:
        break