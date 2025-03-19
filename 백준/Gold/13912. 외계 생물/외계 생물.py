# 백준 13912

'''
2일차일 때를 보면, 총 15마리의 생물이 있고, 루트는 항상 1번이 되어야 하므로 14마리의 생물에 대해 번호를 정해야 한다.
왼쪽 무리와 오른쪽 무리로 나눌 수 있는데, 왼쪽 무리에 들어갈 

DP[i] = i일째일 때, 생물에게 번호를 붙일 수 있는 경우의 수.
DP[1] = 2
DP[2] = 6C3 * (DP[1])^2
DP[3] = 14C7 * (DP[2])^2
...
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
MOD = 1000000007


# nCr 계산
def combination(N, R):
    result = 1
    for i in range(N, R, -1):
        result = result * i // (N-i+1)

    return result


def solve(H):
    DP = [0 for _ in range(11)]
    DP[0] = 1
    DP[1] = 2

    for i in range(2, H+1):
        DP[i] = (combination(2**(i+1)-2, 2**i-1) * (DP[i-1])**2) % MOD
    
    return DP[H]


def main():
    H = int(input())
    print(solve(H))


main()
