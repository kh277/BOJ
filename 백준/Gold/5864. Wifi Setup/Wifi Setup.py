# 백준 5864

'''
N마리의 소가 수직선 위에 있다.
위치 x에 범위가 r인 기지국을 설치하면 [x-r, x+r] 범위에 대해 wifi가 닿을 수 있으며,
A(기지국 설치 비용) + B(거리 당 비용) * r의 돈이 든다.
모든 소에게 wifi가 닿도록 하는 최소 비용을 찾는 문제이다.

DP[i] = i번째 소까지 wifi가 닿도록 할 때, 필요한 최소 비용
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 1e10

def solve():
    DP = [INF for _ in range(N+1)]
    point.sort()

    DP[0] = 0
    DP[1] = A

    # 인덱스가 cur인 소까지 고려
    for cur in range(2, N+1):
        # 새로 설치할 기지국이 before번째 소부터 cur번째 소까지 커버할 경우 
        for before in range(1, cur+1):
            distance = point[cur-1] - point[before-1]
            DP[cur] = min(DP[cur], DP[before-1]+A+B*distance//2)

    return DP[N]


# main 함수 ----------
N, A, B = map(int, input().split())
A *= 2
B *= 2
point = []
for _ in range(N):
    point.append(int(input()))

result = solve()
if result % 2 == 0:
    print(result//2)
else:
    print(result/2)