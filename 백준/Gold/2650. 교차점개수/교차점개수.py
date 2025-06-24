# 백준 2650

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def getRange(p1, x1, p2, x2):
    if p1 == 1:
        # 1 -> 1
        if p2 == 1:
            return [[1, x1, x2]]
        # 1 -> 3
        elif p2 == 3:
            return [[1, 0, x1], [3, 0, x2]]
        # 1 -> 4
        elif p2 == 4:
            return [[1, x1, 50], [4, 0, x2]]
        # 1 -> 2
        else:
            return [[1, 0, x1], [3, 0, 50], [2, 0, x2]]
    elif p1 == 2:
        # 2 -> 2
        if p2 == 2:
            return [[2, x1, x2]]
        # 2 -> 3
        elif p2 == 3:
            return [[2, 0, x1], [3, x2, 50]]
        # 2 -> 4
        else:
            return [[2, x1, 50], [4, x2, 50]]
    elif p1 == 3:
        # 3 -> 3
        if p2 == 3:
            return [[3, x1, x2]]
        # 3 -> 4
        else:
            return [[3, 0, x1], [1, 0, 50], [4, 0, x2]]
    # 4 -> 4
    else:
        return [[4, x1, x2]]


def solve(N, line):
    cross = [0 for _ in range(N+1)]
    for i in range(N):
        for j in range(N):
            if i == j:
                continue

            count = 0
            # 선분 구간 내에 점이 존재하는지 체크
            for p, x1, x2 in getRange(*line[i]):
                if line[j][0] == p and x1 <= line[j][1] <= x2:
                    count += 1
                if line[j][2] == p and x1 <= line[j][3] <= x2:
                    count += 1

            # 선분 내에서 시작해서 선분 외부에서 끝난다면 +1
            if count % 2 == 1:
                cross[i] += 1

    return [sum(cross)//2, max(cross)]


def main():
    N = int(input())
    line = []
    for _ in range(N//2):
        a, b, c, d = map(int, input().split())
        if a > c:
            line.append([c, d, a, b])
        elif a == c:
            line.append([a, min(b, d), c, max(b, d)])
        else:
            line.append([a, b, c, d])

    for i in solve(N//2, line):
        print(i)


main()
