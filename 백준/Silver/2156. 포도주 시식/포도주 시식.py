# 백준 2156번

# 예시입력 : 6 10 13 9 8 1
# 9을 마시는 경우, DP[3]은 max(DP[0] + 13 + 9, DP[1] + 9)임.
# 9를 마시지 않는 경우, DP[3]은 DP[2]와 같은 값을 가짐.
# 따라서 DP[3]의 경우 max(DP[0]+ 13 + 9, DP[1] + 9, DP[2])가 됨.
# ...
# N을 마시는 경우, max(DP[N-3] + N-1 + N, DP[N-2] + N, DP[N-1])이 됨.

from sys import stdin

input = stdin.readline


def solve(N: int, glass: list) -> int:

    # DP[N] = N번째까지 마신 최대의 음료량
    DP = [0 for _ in range(N)]

    DP[0] = glass[0]
    if N > 1:
        DP[1] = glass[0] + glass[1]

    if N > 2:
        DP[2] = max(glass[1] + glass[2], glass[0] + glass[2], glass[0] + glass[1])

    if N > 3:
        for i in range(3, N):
            # 1. N번째 잔을 마시는 경우
            # 1-1. N-1번째 잔을 마시는 경우 -> N-3까지의 합 + N-1 + N
            # 1-2. N-1번째 잔을 마시지 않는 경우 -> N-2까지의 합 + N
            # 2. N번째 잔을 마시지 않는 경우 -> N-1까지의 합
            DP[i] = max(DP[i-3] + glass[i-1] + glass[i], DP[i-2] + glass[i], DP[i-1])
            
    # 인덱스는 0부터 시작되므로 N번째 잔은 DP[N-1]에 저장
    return DP[N-1]


def main():
    N = int(input())
    glass = [None for _ in range(N)]

    for i in range(N):
        glass[i] = int(input())

    print(solve(N, glass))


main()
