# 백준 1947

'''
DP[i] = i명에 대한 교란순열
'''

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
MOD = 1000000000


def solve(N):
    DP = array('I', [0]) * (N+1)
    for i in range(2, N+1):
        if i & 1:
            DP[i] = (i*DP[i-1] - 1) % MOD
        else:
            DP[i] = (i*DP[i-1] + 1) % MOD
    
    return DP[N]


def main():
    N = int(input())
    print(solve(N))


main()
