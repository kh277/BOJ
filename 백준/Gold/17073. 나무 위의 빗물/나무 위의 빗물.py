# 백준 17073

'''
고인 물의 기대값은 W / (리프 노드의 개수)이다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline

def solve(N, graph):
    result = 0
    for i in range(2, N+1):
        if len(graph[i]) == 1:
            result += 1

    return result


def main():
    N, W = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    print(W/solve(N, graph))


main()
