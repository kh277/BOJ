# 백준 1303

'''
1. (0, 0) ~ (N-1, M-1)까지 순서대로 탐색하되, 방문하지 않은 정점인 경우 큐에 삽입
2-1. 큐에서 한 정점을 꺼냄 (카운트 +1)
2-2. 그 정점의 상하좌우 좌표 탐색 (양 끝 경계선 좌표 주의)
2-3. 상하좌우 좌표 중 꺼낸 정점과 같은 진영만 큐에 다시 삽입
2-4. 큐가 빌 때까지 반복
'''


from sys import stdin
from queue import Queue

input = stdin.readline


def solve(N: int, M: int, board: list) -> list:
    visited = [[False for _ in range(N)] for _ in range(M)]
    white_count = 0
    blue_count = 0

    queue = Queue()

    # 1. (0, 0)부터 (N-1, M-1)까지 탐색
    for i in range(M):
        for j in range(N):
            # 방문하지 않은 정점인 경우 -> 큐에 삽입
            if visited[i][j] == False:
                queue.put((i, j))
                visited[i][j] = True  # 방문했다고 표시
            else:
                continue

            # 2. 큐가 빌 때까지 반복
            count = 0
            while not queue.empty():
                # 2-1. 큐에서 한 정점을 꺼냄
                a, b = queue.get()
                camp = board[a][b]      # 진영 확인
                count += 1

                # 2-2. 그 정점의 상하좌우 좌표 탐색, 같은 진영만 큐에 다시 삽입
                for x, y in queue_input(a, b, N, M):
                    if visited[x][y] == False and camp == board[x][y]:
                        queue.put((x, y))
                        visited[x][y] = True

            if camp == 'W':
                white_count += count**2
            else:
                blue_count += count**2

    return [white_count, blue_count]


def queue_input(a: int, b: int, N: int, M: int) -> list:
    array = []

    if not a == 0:
        array.append((a-1, b))
    if not b == 0:
        array.append((a, b-1))
    if not a == M-1:
        array.append((a+1, b))
    if not b == N-1:
        array.append((a, b+1))

    return array


def main():
    N, M = map(int, input().split())

    board = [None for _ in range(M)]
    for i in range(M):
        board[i] = list(input().rstrip())

    print(*solve(N, M, board))


main()
