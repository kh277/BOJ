# 백준 14567

'''
위상 정렬에서 진입차수의 최대값을 구하자.
'''

import sys
from collections import deque

input = sys.stdin.readline


def solve(V: int, graph: list) -> list:
    inDegree = [0 for _ in range(V+1)]

    # A < B인 입력만 주어지므로 정렬 가능
    graph.sort(key= lambda x: [x[0], x[1]])

    # 각 정점의 진입차수 설정
    for i in graph:
        inDegree[i[1]] = max(inDegree[i[0]] + 1, inDegree[i[1]])
    
    # 학기는 1학기부터 시작이므로 모든 값에 +1
    return [i+1 for i in inDegree][1:]


def main():
    N, M = map(int, input().split())
    
    graph = []
    for _ in range(M):
        A, B = map(int, input().split())
        graph.append([A, B])

    print(*solve(N, graph))


main()