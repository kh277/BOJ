# 백준 11054

'''
11053번 LIS 문제와 같다.

증감이 변화하는 k번째 원소의 위치가 0번째 일때부터 N번째 일때까지 변화시키며 최대값을 찾는다.
다만, 증가하는 부분에서는 LIS에 대한 DP테이블을,
감소하는 부분에서는 배열을 뒤집어 LIS에 대한 DP테이블을 구한다.
구한 DP테이블을 통해 0부터 N까지의 LIS 길이를 구한다.
이후 0부터 N까지 k값을 변화시키며 바이토닉 수열 길이를 구한다.
'''

import sys

input = sys.stdin.readline


def LIS(N: int, A: list) -> list:
    DP = [1 if A[i] != -1 else -1 for i in range(N)]

    # 현재 탐색하고자 하는 값
    for i in range(N):
        # 이전 값들의 LIS 탐색
        for j in range(0, i):
            if A[i] > A[j] and DP[i] != -1:
                DP[i] = max(DP[i], DP[j] + 1)

    return DP


def solve(N: int, A: list) -> int:

    inc = LIS(N, A)
    dec = LIS(N, list(reversed(A)))

    # 0~i번째 원소까지의 LIS값 저장
    # 주의 - DP테이블이랑 LIS값이랑은 다름!
    max_inc = 0
    max_dec = 0
    for i in range(N):
        if max_inc < inc[i]:
            max_inc = inc[i]
        else:
            inc[i] = max_inc
        if max_dec < dec[i]:
            max_dec = dec[i]
        else:
            dec[i] = max_dec

    # 바이토닉 부분 수열 계산
    result = 0
    for i in range(N):
        if result < inc[i] + dec[N-i-1]:
            result = inc[i] + dec[N-i-1]

    # 증감이 바뀌는 부분은 중복되었으므로 -1
    return result - 1


def main():
    N = int(input())
    A = list(map(int, input().split()))

    print(solve(N, A))


main()
