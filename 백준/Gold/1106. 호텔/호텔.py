# 백준 1106

'''
DP 테이블의 가로축을 목표 수(j), 세로축을 도시(i)로 보면,
DP[i][j] = 0~i번째 도시까지 투자해서 j명을 늘리는데 드는 돈의 최소값.

다만, 적어도 C명을 구해야 하므로 DP[N-1][C]보다 큰 C 값에서 최소값이 나올 수도 있다.
홍보로 얻을 수 있는 고객의 수는 최대 99명이므로 C의 한계값인 1000에 100을 더한 값까지 계산하자.

주의 반례
5 3
1 5
6 5
2 1
-> 1

1000 1
1 99
-> 11
'''

import sys

input = sys.stdin.readline
INF = 10e6


def solve(C: int, N: int, data: list) -> int:
    max_data = min(C+100, 1100)
    DP = [[INF for _ in range(max_data)] for _ in range(N)]

    for i in range(N):
        for j in range(1, max_data):
            if j == data[i][1]:
                DP[i][j] = min(DP[i-1][j], data[i][0])
            else:
                DP[i][j] = min(DP[i-1][j], DP[i][j-data[i][1]] + data[i][0])

    return min(DP[N-1][C:])


def main():
    C, N = map(int, input().split())

    data = []
    for _ in range(N):
        data.append(list(map(int, input().split())))
    
    print(solve(C, N, data))


main()
