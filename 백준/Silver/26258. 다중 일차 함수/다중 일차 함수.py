# 백준 26258

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def query(N, point, target):
    start = 0
    end = N-1

    while start < end:
        mid = (start+end)//2
        if point[mid][0] < target:
            start = mid+1
        else:
            end = mid

    if point[start-1][0] == point[start][0]:
        return 0
    slope = (point[start][1]-point[start-1][1])/(point[start][0]-point[start-1][0])
    if slope > 0:
        return 1
    elif slope < 0:
        return -1
    return 0


def main():
    N = int(input())
    point = []
    for _ in range(N):
        point.append(list(map(int, input().split())))
    Q = int(input())
    for _ in range(Q):
        k = float(input())
        print(query(N, point, k))


main()
