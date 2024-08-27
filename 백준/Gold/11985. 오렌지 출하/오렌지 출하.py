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


def solve(N: int, M: int, K: int, orange: list) -> int:
    DP = [0 for _ in range(N+1)]

    for i in range(1, N+1):
        temp = []
        for j in range(1, M+1):
            if i < j:
                continue
            # 1~(i-j)번째 까지 오렌지 최소값 + (i-j+1)~i번째까지 오렌지를 한 상자에 담았을 때의 값
            temp.append(DP[i-j] + K + j*(max(orange[i-j+1:i+1]) - min(orange[i-j+1:i+1])))
        DP[i] = min(temp)

    return DP[-1]


def main():
    N, M, K = map(int, input().split())
    orange = [0]
    for _ in range(N):
        orange.append(int(input()))
    
    print(solve(N, M, K, orange))


main()
