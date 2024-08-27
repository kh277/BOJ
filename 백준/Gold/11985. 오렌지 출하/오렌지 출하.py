# 백준 11985

'''
DP 테이블의 가로축은 i번 오렌지로 표현된다.
DP[i] = i번째 오렌지까지 넣었을 때의 최소 비용

ex) M=3이라고 가정했을 때,
DP[i] = min((DP[i-1] + 상자에 i번째 오렌지를 넣는 경우),
            (DP[i-2] + 상자에 (i-1)~i번째 오렌지를 넣는 경우),
            (DP[i-3] + 상자에 (i-2)~i번째 오렌지를 넣는 경우))
'''

import sys

input = sys.stdin.readline
INF = 10e13


def solve(N: int, M: int, K: int, orange: list) -> int:
    DP = [INF for _ in range(N+1)]
    DP[0] = 0

    for i in range(1, N+1):
        for j in range(1, M+1):
            # 음수 인덱스를 참조하게 되는 경우 탈출
            if i < j:
                break

            # 최대값 및 최소값 찾기
            max_data = max(orange[i-j+1:i+1])
            min_data = min(orange[i-j+1:i+1])
                
            # 1~(i-j)번째 까지 오렌지 최소값 + (i-j+1)~i번째까지 오렌지를 한 상자에 담았을 때의 값
            # 이전에 저장한 값과 비교하여 갱신
            DP[i] = min(DP[i], DP[i-j] + K + j*(max_data - min_data))

    return DP[N]


def main():
    N, M, K = map(int, input().split())
    orange = [0]
    for _ in range(N):
        orange.append(int(input()))
    
    print(solve(N, M, K, orange))


main()
