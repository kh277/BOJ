# 백준 2886

'''
모든 사람들은 가장 가까운 자리를 노린다.
노리는 자리까지의 거리보다 더 가까운 사람이 있다면, 다음으로 가까운 자리를 노린다.
따라서 모든 사람-의자 간 간선을 저장하고, 제일 거리가 적은 간선부터 그리디하게 배정하면 된다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**6


def solve(Y, X, grid):
    # 'L', 'X'의 위치 파악
    seat = []
    player = []
    for y in range(Y):
        for x in range(X):
            if grid[y][x] == 'L':
                seat.append((y, x))
            elif grid[y][x] == 'X':
                player.append((y, x))

    # 각각의 'X'에 대해 모든 'L'까지의 거리 저장
    data = []
    for i in range(len(seat)):
        sY, sX = seat[i]
        for j in range(len(player)):
            pY, pX = player[j]
            data.append((i, j, (pY - sY)**2 + (pX - sX)**2))

    # 거리가 짧은거부터 그리디하게 배치, 이미 자리를 잡은 사람은 넘기기
    seatData = [[INF, 0] for _ in range(len(seat))]
    visited = [0 for _ in range(len(player))]
    data.sort(key= lambda x: (x[2]))
    for curS, curP, dist in data:
        if visited[curP] == 0 and seatData[curS][0] > dist:
            seatData[curS][0] = dist
            seatData[curS][1] = 1
            visited[curP] = 1
        elif visited[curP] == 0 and seatData[curS][0] == dist:
            seatData[curS][1] += 1
            visited[curP] = 1

    # 충돌 개수 세기
    result = 0
    for i in range(len(seat)):
        if seatData[i][1] > 1:
            result += 1

    return result


def main():
    Y, X = map(int, input().split())
    grid = []
    for _ in range(Y):
        grid.append(list(input().decode().strip()))
    print(solve(Y, X, grid))


main()
