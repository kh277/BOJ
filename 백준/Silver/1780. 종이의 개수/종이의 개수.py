# 백준 1780

'''
분할 정복을 이용하여 9개의 조각으로 나누면서 -1, 0, 1의 개수를 반환한다.
'''


import sys

input = sys.stdin.readline


def check(N: int, graph: list) -> list:
    init = graph[0][0]
    for i in range(N):
        for j in range(N):
            if graph[i][j] != init:
                return [False, None]
    
    return [True, init]


def solve(N: int, graph: list) -> list:
    # 해당 그래프가 전부 같은 숫자인지 확인
    temp = check(N, graph)
    if temp[0]:
        if temp[1] == -1:
            return [1, 0, 0]
        elif temp[1] == 0:
            return [0, 1, 0]
        else:
            return [0, 0, 1]
    
    # 9분할 후 확인
    result = []
    result.append(solve(N//3, [i[:N//3] for i in graph[:N//3]]))
    result.append(solve(N//3, [i[N//3:2*N//3] for i in graph[:N//3]]))
    result.append(solve(N//3, [i[2*N//3:] for i in graph[:N//3]]))
    result.append(solve(N//3, [i[:N//3] for i in graph[N//3:2*N//3]]))
    result.append(solve(N//3, [i[N//3:2*N//3] for i in graph[N//3:2*N//3]]))
    result.append(solve(N//3, [i[2*N//3:] for i in graph[N//3:2*N//3]]))
    result.append(solve(N//3, [i[:N//3] for i in graph[2*N//3:]]))
    result.append(solve(N//3, [i[N//3:2*N//3] for i in graph[2*N//3:]]))
    result.append(solve(N//3, [i[2*N//3:] for i in graph[2*N//3:]]))

    # 결과 총합 후 리턴
    for i in range(1, 9):
        result[0][0] += result[i][0]
        result[0][1] += result[i][1]
        result[0][2] += result[i][2]
    
    return result[0]


def main():
    N = int(input())
    graph = []
    
    for _ in range(N):
        graph.append(list(map(int, input().split())))
    
    for i in solve(N, graph):
        print(i)

main()