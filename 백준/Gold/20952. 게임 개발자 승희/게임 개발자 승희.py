# 백준 20952

'''
(A[i] % 7) + leftMod == 7 이 되는 leftMod의 값을 전부 저장해둔다.
B[j] % 7을 계산한 값과 같은 leftMod값을 가지는 수들은 7로 나눌 수 있으므로 전부 지울 수 있다.
남은 leftMod 종류가 하나만 존재할 경우의 케이스만 주의해서 처리하면 된다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
MOD = 7000000049


def solve(N, M, A, B):
    leftMod = set()    # A에 있는 수들의 mod
    for i in range(N):
        leftMod.add((7 - (A[i] % 7)) % 7)

    # A의 나머지가 한 종류인 경우
    if len(leftMod) == 1:
        leftMod = list(leftMod)[0]
        add = 0
        for i in range(M):
            if B[i] % 7 != leftMod:
                add = (add + B[i]) % MOD

        result = [(i + add) % 1000000007 for i in A]

    # A의 나머지가 두 종류 이상인 경우
    else:
        delMod = set()    # A에서 제거될 수들의 mod
        curMod = 0
        add = 0
        for i in range(M):
            prevMod = curMod
            curMod = (curMod + B[i]) % 7
            # 나머지가 한 종류밖에 없어 제거할 수 없는 경우
            if len(leftMod) == 1 and curMod in leftMod:
                curMod = prevMod
                continue
            # 그 외 경우
            else:
                if curMod in leftMod:
                    leftMod.remove(curMod)
                    add = (add + B[i]) % MOD
                    delMod.add((7 - (add % 7)) % 7)
                else:
                    add = (add + B[i]) % MOD

        result = []
        for i in range(N):
            if A[i] % 7 not in delMod:
                result.append((A[i]+add) % 1000000007)

    return [[len(result)], result]


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    for i in solve(N, M, A, B):
        print(*i)


main()
