# 백준 19884

'''
이진 트리에 루트부터 내림차순으로 그리디하게 배치한 후 자식 정점과의 차이가 K 이하인지 체크하면 된다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, K, sword):
    sword.sort(key= lambda x: (-x[0], x[1]))
    result = [-1 for _ in range(N)]
    result[sword[1][1]] = 0
    for i in range(1, N+1):
        cur, index = sword[i]
        if (i<<1) <= N:
            if cur >= K + sword[i<<1][0]:
                result[sword[i<<1][1]] = index
        if (i<<1 | 1) <= N:
            if cur >= K + sword[i<<1 | 1][0]:
                result[sword[i<<1 | 1][1]] = index

    for i in range(N):
        if result[i] > -1:
            result[i] += 1
        if result[i] == -1:
            return [-1]
    result[sword[1][1]] = 0

    return result


def main():
    N, K = map(int, input().split())
    sword = [[10**10, -1]]
    for i, v in enumerate(list(map(int, input().split()))):
        sword.append([v, i])

    print(*solve(N, K, sword))


main()
