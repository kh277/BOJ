# 백준 23104

'''
DP[y][x] = y번째 종이의 x번째 수를 시작으로 하는 감소하지 않는 수열의 개수
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
MOD = 1000000007


def solve(N, K, paper):
    DP = [[0 for _ in range(K)] for _ in range(N)]
    
    # 초기값 설정
    for x in range(K):
        DP[N-1][x] = 1
    
    # DP 계산
    for y in range(N-2, -1, -1):
        # 투 포인터로 계산 최적화
        p = 0
        accDP = 0
        for x in range(K):
            while p < K and paper[y][x] <= paper[y+1][p]:
                accDP += DP[y+1][p]
                p += 1
            DP[y][x] = accDP % MOD

    return sum(DP[0]) % MOD


def main():
    N, K = map(int, input().split())
    paper = []
    for _ in range(N):
        paper.append(sorted(list(map(int, input().split())), reverse=True))

    print(solve(N, K, paper))


main()