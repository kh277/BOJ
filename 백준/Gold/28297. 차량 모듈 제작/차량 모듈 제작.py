# 백준 28297

import io
import math

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


# 기어A와 기어B를 벨트로 이을 경우 필요한 벨트 길이 반환
def getBeltSize(gearA, gearB):
    x1, y1, r1 = gearA
    x2, y2, r2 = gearB
    d2 = (x1-x2)**2 + (y1-y2)**2
    r = (r1-r2)

    if d2 <= (r1+r2)**2:
        return 0

    # 선분 부분 길이
    line = (d2-r*r)**0.5

    # 곡선 부분 길이
    arcsin = math.degrees(math.asin((r*r/d2)**0.5))
    circle = math.pi * (180*r1 + 180*r2 + 2*r1*arcsin - 2*r2*arcsin) / 180

    return 2*line + circle


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])

    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    parent[max(a, b)] = min(a, b)


def solve(N, gear):
    # 기어 간 필요한 벨트를 간선의 가중치로 설정
    edge = []
    for i in range(N-1):
        for j in range(i+1, N):
            if gear[i][2] >= gear[j][2]:
                edge.append((i, j, getBeltSize(gear[i], gear[j])))
            else:
                edge.append((i, j, getBeltSize(gear[j], gear[i])))

    # 크루스칼 알고리즘으로 MST 구하기
    result = 0
    parent = [i for i in range(N+1)]
    edge.sort(key= lambda x: x[2])

    for cur in edge:
        startV, endV, cost = cur
        if find(parent, startV) != find(parent, endV):
            union(parent, startV, endV)
            result += cost

    return result


def main():
    N = int(input())
    gear = []
    for _ in range(N):
        gear.append(tuple(map(int, input().split())))

    print(solve(N, gear))


main()
