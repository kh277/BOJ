# 백준 1980

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**5


def solve(N, M, T):
    coke = INF
    hamb = 0
    for x in range(T//N+1):
        for y in range(T//M+1):
            cur = N*x + M*y
            if cur <= T and coke > T-cur:
                coke = T-cur
                hamb = x+y
            elif cur <= T and coke == T-cur:
                hamb = max(hamb, x+y)
            elif cur > T:
                break
    
    return [hamb, coke]


def main():
    N, M, T = map(int, input().split())
    print(*solve(N, M, T))


main()
