# 백준 1351

'''
N의 값이 최대 10^12이기 때문에 단순 리스트로 적용할 경우 시간초과가 발생한다.
재귀를 반복할 경우 N이 지수적으로 작아지므로 필요한 값에 대해서만 반복하자.

또한 값의 중복계산을 줄이기 위해 딕셔너리에 키-값을 저장하자.
'''

import sys

input = sys.stdin.readline


def recur(N: int, P: int, Q: int, DP: dict) -> int:
    if N == 0:
        return 1

    if N//P not in DP:
        DP[N//P] = recur(N//P, P, Q, DP)
    if N//Q not in DP:
        DP[N//Q] = recur(N//Q, P, Q, DP)
    
    return DP[N//P] + DP[N//Q]


def main():
    N, P, Q = map(int, input().split())
    print(recur(N, P, Q, dict()))
    

main()