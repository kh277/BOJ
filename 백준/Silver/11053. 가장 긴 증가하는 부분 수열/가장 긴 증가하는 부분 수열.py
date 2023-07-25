# 백준 11053

'''
k+1 ~ N까지의 수 중에서 A[K]보다 큰 값에 l에 대해 A[K] + 1 or A[l]
0  1  2  3  4  5  <- A의 인덱스
10 20 10 30 20 50
1  1  1  1  1  1  <- DP의 기본값은 1
   1     1  1  1  <- 10보다 큰 값은 +1
         1     1  <- 20보다 큰 값은 +1
         -  -  -  <- k번째 수에 대해, max(A[2] + 1, A[k])
               1  <- 30보다 큰 값은 +1

'''
from sys import stdin

input = stdin.readline


def solve(N: int, A: list) -> int:
    maxNum = 1

    # DP[x] = x번째까지의 증가하는 부분 수열 중 최대 길이
    DP = [1 for _ in range(N)]

    for x in range(N-1):
        for y in range(x+1, N):
            if A[x] < A[y]:
                DP[y] = max(DP[x] + 1, DP[y])
                if DP[y] > maxNum:
                    maxNum = DP[y]

    return maxNum


def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(solve(N, A))


main()
