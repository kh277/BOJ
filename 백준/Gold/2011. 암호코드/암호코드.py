# 백준 2011

'''
DP[i] = 문자열의 i번째 자리까지 생각할 때, 가능한 암호의 개수
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
MOD = 1000000


def solve(A) -> int:
    length = len(A)

    # 맨 앞에 0이 오는 경우
    if A[0] == '0':
        return 0

    DP = [0 for _ in range(length+1)]
    DP[0] = 1
    DP[1] = 1

    for i in range(2, length+1):
        # 00이 연속해서 오는 경우
        if A[i-2:i] == '00':
            return 0

        # 현재 계산해야 하는 자리가 0인 경우
        if A[i-1] == '0':
            if A[i-2] in ['1', '2']:
                DP[i] = DP[i-2]
                continue
            else:
                return 0

        # 현재 계산해야 하는 자리의 앞자리가 0이 아닌 경우
        if A[i-2] != '0':
            if 1 <= int(A[i-2:i]) <= 26:
                DP[i] = (DP[i] + DP[i-2]) % MOD
            elif A[i-2:i] in ['10', '20']:
                DP[i] = DP[i-2]
            if int(A[i-1]) != 0:
                DP[i] = (DP[i] + DP[i-1]) % MOD
        # 현재 계산해야 하는 자리의 앞자리가 0인 경우
        else:
            DP[i] = DP[i-1]

    return DP[length]


def main():
    A = input().decode().rstrip()
    print(solve(A))


main()