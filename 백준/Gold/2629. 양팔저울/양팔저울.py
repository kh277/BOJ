# 백준 2629

'''
DP[i][j] = 0~i번째 추까지 사용하여 무게 j를 나타낼 수 있는지 여부
'''

import sys

input = sys.stdin.readline

def solve():
    DP = [[False for _ in range(sum(weight)+1)] for _ in range(N)]
    DP[0][weight[0]] = True
    limit = weight[0]
    
    # DP 처리
    for i in range(1, N):
        DP[i][weight[i]] = True     # 현재 추의 무게 True
        for j in range(limit+1):
            if DP[i-1][j] == True:  # 이전까지 나타낼 수 있는 무게 +- 현재 추
                DP[i][j] = True
                DP[i][weight[i]+j] = True
                if weight[i] - j > 0:
                    DP[i][weight[i]-j] = True
                else:
                    DP[i][j-weight[i]] = True
        limit += weight[i]

    # 쿼리 처리
    result = ""
    for i in range(Q):
        if query[i] > limit:
            result += "N "
        elif DP[N-1][query[i]] == True:
            result += "Y "
        else:
            result += "N "
    return result.rstrip()


# main ----------
N = int(input())
weight = list(map(int, input().split()))

Q = int(input())
query = list(map(int, input().split()))

print(solve())