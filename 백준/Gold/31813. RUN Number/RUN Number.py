# 백준 31813

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, K):
    result = []
    while True:
        strK = str(K)
        lenK = len(strK)

        # 종료조건
        if lenK == 1:
            if K == 0:
                return [[len(result)], result]
            result.append(K)
            return [[len(result)], result]

        # 앞자리가 1일 경우
        if strK[0] == '1':
            if K < int('1' * lenK):
                cur = int('9' * (lenK-1))
                K -= cur
                result.append(cur)
            else:
                cur = int('1' * lenK)
                K -= cur
                result.append(cur)

        # 앞자리가 1이 아닐 경우
        else:
            first = strK[0]
            if K < int(first * lenK):
                cur = int(str(int(first)-1) * lenK)
                K -= cur
                result.append(cur)
            else:
                cur = int(first * lenK)
                K -= cur
                result.append(cur)


def main():
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        for i in solve(N, K):
            print(*i)


main()
