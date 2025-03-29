# 백준 9251

'''
A, B 문자열은 최대 1000글자로 이루어져 있으므로 O(N^2)에 해결할 수 있다.
DP[i][j] = A문자열의 i번째, B문자열의 j번째까지의 LCS 값이라고 하자.
'''

import sys

input = sys.stdin.readline

def solve(A: str, B: str) -> int:
    # 인덱스는 1부터 시작
    DP = [[0 for _ in range(len(B)+1)] for _ in range(len(A)+1)]

    for i in range(1, len(A)+1):
        for j in range(1, len(B)+1):
            if A[i-1] == B[j-1]:
                DP[i][j] = DP[i-1][j-1] + 1
            else:
                DP[i][j] = max(DP[i-1][j], DP[i][j-1])


    return DP[len(A)][len(B)]


def main():
    A = input().rstrip()
    B = input().rstrip()

    print(solve(A, B))


main()