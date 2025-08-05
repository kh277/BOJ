# 백준 21757

'''
먼저, 수열 A의 총합을 0, 4의 배수, 4의 배수가 아닌 경우로 나누어 처리한다.

총합이 4의 배수인 경우, 수열 A의 총합이 4K라고 두자.
이 때, 누적합 배열에서 값이 K, 2K, 3K인 위치를 순서대로 선택하는 경우의 수를 O(N)으로 계산하면 된다.

총합이 0의 배수인 경우, 맨 마지막 0은 고정이므로, 누적합 배열에서 0을 3개 선택하는 경우의 수와 같다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, L):
    allSum = sum(L)

    # 누적합 계산
    accSum = [L[0]]
    for i in range(1, N):
        accSum.append(accSum[i-1] + L[i])

    # 합이 0일 경우
    if allSum == 0:
        zeroCount = sum([1 for i in range(N) if accSum[i] == 0]) - 1
        return zeroCount*(zeroCount-1)*(zeroCount-2)//6

    # 합이 4의 배수가 아닐 경우
    elif allSum % 4 != 0:
        return 0

    # 합이 4의 배수일 경우
    K1 = allSum//4
    K2 = K1*2
    K3 = K1*3

    # DP 계산
    DP1 = [0 for _ in range(N)]
    DP2 = [0 for _ in range(N)]
    DP3 = [0 for _ in range(N)]
    if accSum[0] == K1:
        DP1[0] += 1

    for i in range(1, N):
        DP1[i] = DP1[i-1]
        if accSum[i] == K1:
            DP1[i] += 1
        
        DP2[i] = DP2[i-1]
        if accSum[i] == K2:
            DP2[i] += DP1[i]
        
        DP3[i] = DP3[i-1]
        if accSum[i] == K3:
            DP3[i] += DP2[i]

    return DP3[N-1]


def main():
    N = int(input())
    L = list(map(int, input().split()))
    print(solve(N, L))


main()
