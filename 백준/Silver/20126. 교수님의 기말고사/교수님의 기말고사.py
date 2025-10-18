# 백준 20126

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**10


def solve(N, M, S, data):
    data.sort()

    # 0초에 배치가 가능한 경우
    if M <= data[0][0]:
        return 0

    # 시험이 끝나고 배치가 가능한지 체크
    for i in range(N-1):
        if data[i][1] + M <= data[i+1][0]:
            return data[i][1]

    # 모든 시험이 끝나고 배치가 가능한 경우
    if data[N-1][1] + M <= S:
        return data[-1][1]

    return -1


def main():
    N, M, S = map(int, input().split())
    data = []
    for _ in range(N):
        a, b = map(int, input().split())
        data.append([a, a+b])
    print(solve(N, M, S, data))


main()
