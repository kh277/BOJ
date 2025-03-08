# 백준 11390

import io
import math

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(A, B, N, K):
    # 높이 A가 밑변 B보다 작은 상태를 가정하고 계산했음
    A, B = min(A, B), max(A, B)

    # nCk일 때의 이항 계수 전부 계산
    nC = [1]
    for i in range(1, N+1):
        nC.append(nC[i-1] * (N+1-i) // i)

    # 넓이 찾기
    for i in range(N+1):
        if K <= nC[i]:
            # 점화식을 통해 넓이 계산
            result = A * B * (A**2/(A**2+B**2))**i * (B**2/(A**2+B**2))**(N-i) / 2
            return math.log(result)
        else:
            K -= nC[i]


def main():
    A, B, N, K = map(int, input().split())
    print(solve(A, B, N, K))


main()