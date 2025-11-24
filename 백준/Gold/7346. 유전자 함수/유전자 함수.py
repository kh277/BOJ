# 백준 7346

'''
DP[i][j] = 첫 번째 서열을 i번째까지 비교했고 두 번째 서열을 j번째까지 비교했을 때, 유사도의 최대값
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
t = {'A': 0, 'C': 1, 'G': 2, 'T': 3, '*': 4}
value = [(5, -1, -2, -1, -3),
        (-1, 5, -3, -2, -4),
        (-2, -3, 5, -2, -2),
        (-1, -2, -2, 5, -1),
        (-3, -4, -2, -1, -10**8)]


def solve(A, B):
    lenA = len(A)
    lenB = len(B)
    DP = [[0 for _ in range(lenB+1)] for _ in range(lenA+1)]
    for y in range(1, lenA+1):
        DP[y][0] = DP[y-1][0] + value[A[y-1]][4]
    for x in range(1, lenB+1):
        DP[0][x] = DP[0][x-1] + value[4][B[x-1]]

    for y in range(1, lenA+1):
        for x in range(1, lenB+1):
            # A와 *을 매칭하는 경우, *과 B를 매칭하는 경우, A와 B를 매칭하는 경우
            DP[y][x] = max(DP[y-1][x] + value[A[y-1]][4], DP[y][x-1] + value[4][B[x-1]], DP[y-1][x-1] + value[A[y-1]][B[x-1]])

    return DP[lenA][lenB]


def main():
    T = int(input())
    for _ in range(T):
        _, A = input().decode().split()
        _, B = input().decode().split()
        A = [t[i] for i in A]
        B = [t[i] for i in B]

        print(solve(A, B))


main()
