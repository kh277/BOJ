# 백준 3262

'''
약품 상자가 있는 구간에 폭탄이 터질 경우, 해당 범위의 값에 +1을 해준다.
약품 상자가 있는 곳은 T=1인 쿼리의 개수와 같은 값을 가진 위치가 된다.
만약 T=0인 쿼리만 들어왔을 경우, 약품 상자가 있는 위치는 미탐색 지역에 존재하게 된다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(A, B, K, data):
    grid = [[0 for _ in range(B)] for _ in range(A)]

    count = 0
    for i in range(K):
        midY, midX, R, isBox = data[i]
        startX = max(0, midX-1 - (R-1)//2)
        endX = min(B-1, midX-1 + (R-1)//2)
        startY = max(0, midY-1 - (R-1)//2)
        endY = min(A-1, midY-1 + (R-1)//2)

        if isBox == 1:
            count += 1

        # 폭탄 범위 처리
        for y in range(startY, endY+1):
            for x in range(startX, endX+1):
                if isBox == 1 and grid[y][x] != -1:
                    grid[y][x] += isBox
                else:
                    grid[y][x] = -1

    # count인 곳 세기
    result = 0
    notSearch = 0
    for y in range(A):
        for x in range(B):
            if grid[y][x] == count:
                result += 1
            elif grid[y][x] == 0:
                notSearch += 1

    return notSearch if result == 0 and count == 0 else result


def main():
    A, B, K = map(int, input().split())
    data = []
    for _ in range(K):
        data.append(list(map(int, input().split())))

    print(solve(A, B, K, data))


main()
