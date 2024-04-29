# 백준 2098

'''
외판원 문제이지만, 2 <= N <= 10이므로 브루트포스로도 풀린다.
1. 방문하지 않은 next 도시들에 대해 here -> next -> start 로 돌아오는 비용을 계산한다.
2. 재귀를 통해 방문 도시를 늘려가며 반복한다.
3. 모든 도시를 방문할 때까지 1~2번을 반복한다.

주의 반례 :
4
0 1 0 0
0 0 1 0
0 0 0 1
1 0 0 0
'''

import sys

input = sys.stdin.readline


# next를 방문했는지 확인
def check_visit(status: int, city: int) -> bool:
    if status & (1 << city):
        return True
    return False


def TSP(N: int, graph: list, status: int, here: int, DP: list) -> int:
    # 도시를 다 방문한 경우
    # 경로가 존재한다면 here -> start로 가는 값 반환
    # 경로가 존재하지 않는다면 매우 큰 값 반환
    if status == (1 << N) - 1:
        return graph[here][0] if graph[here][0] != 0 else 10e8
    
    # 이전에 계산한 값이면 그 값 반환
    if not DP[here][status] == -1:
        return DP[here][status]

    DP[here][status] = 10e8

    # 방문하지 않은 도시들에 대해 반복
    for next in range(0, N):
        if not check_visit(status, next) and not graph[here][next] == 0:
            # (here에서 next로 가는 비용) + (next에서 나머지 도시를 거쳐 start로 가는 비용) 계산
            # status에서 next 위치를 0으로 변경
            temp = graph[here][next] + TSP(N, graph, status | (1 << next), next, DP)

            # 최소값 갱신이 가능하다면 갱신
            if temp < DP[here][status]:
                DP[here][status] = temp
    
    return DP[here][status]


def solve(N: int, graph: list) -> int:
    DP = [[-1 for _ in range(2**N)] for _ in range(N)]
    
    # 순회 문제이기 때문에 시작 지점은 어디를 잡든지 상관이 없음
    # 이 코드에서는 시작점을 0으로 잡았음
    return TSP(N, graph, 1, 0, DP)


def main():
    N = int(input())
    graph = []

    for i in range(N):
        graph.append(list(map(int, input().split())))
    
    print(solve(N, graph))


main()
