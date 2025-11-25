# 백준 33706

'''
자기 정점보다 작은 정점과의 간선이 존재하는지 보면 된다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, M, edge):
    isConnect = [False for _ in range(N+1)]
    for _, e in edge:
        isConnect[e] = True

    for i in range(2, N+1):
        if isConnect[i] == False:
            return 'NO'
    return 'YES'


def main():
    N, M = map(int, input().split())
    edge = []
    for _ in range(M):
        edge.append(list(map(int, input().split())))
    print(solve(N, M, edge))


main()
