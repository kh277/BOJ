# 백준 11558

import sys

input = sys.stdin.readline


def solve(N: int, graph: list) -> int:
    count = 1
    cur = 1

    while True:
        # 어떤 숫자를 말해도 주경이가 걸리지 않을 경우
        if count > N+1:
            return 0
        
        next = graph[cur][0]

        # 다음 지목이 주경이일 경우
        if next == N:
            return count
            
        count += 1
        cur = next


def main():
    T = int(input())
    
    for _ in range(T):
        N = int(input())
        graph = [[] for i in range(N+1)]
        for i in range(1, N+1):
            A = int(input())
            graph[i].append(A)

        print(solve(N, graph))


main()