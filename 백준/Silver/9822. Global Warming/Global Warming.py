# 백준 9822

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, data):
    data = sorted(data, reverse=True)
    result = 0
    count = 0
    visited = bytearray([0] * N)

    index = 0
    while index < N:
        curH = data[index][0]

        # 높이가 curH인 땅 전부 방문처리
        while index < N and data[index][0] == curH:
            nextX = data[index][1]
            visited[nextX] = 1

            # 주변 땅의 활성화 여부 파악
            neighbor = 0
            if nextX-1 >= 0:
                neighbor += visited[nextX-1]
            if nextX+1 < N:
                neighbor += visited[nextX+1]

            # 섬의 개수 변화 체크
            if neighbor == 0:
                count += 1
            elif neighbor == 2:
                count -= 1

            index += 1

        result = max(result, count)

    return result


def main():
    N = int(input())
    data = []
    for i in range(N):
        data.append([int(input()), i])

    print(solve(N, data))


main()
