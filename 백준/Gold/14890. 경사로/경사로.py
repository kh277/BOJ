# 백준 14890

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def canWalk(N, L, A):
    addSlope = [False for _ in range(N)]
    cur = 0
    while cur < N-1:
        # 같을 경우
        if A[cur] == A[cur+1]:
            cur += 1
        # 1칸 증가할 경우
        elif A[cur] + 1 == A[cur+1]:
            for i in range(cur, cur-L, -1):
                if i < 0 or A[i] != A[cur] or addSlope[i] == True:
                    return False
            cur += 1
        # 1칸 감소할 경우
        elif A[cur] - 1 == A[cur+1]:
            for i in range(cur+1, cur+L+1):
                if i >= N or A[i] != A[cur+1]:
                    return False
            for i in range(cur+1, cur+L+1):
                addSlope[i] = True
            cur += L
        # 2칸 이상 차이날 경우
        else:
            return False

    return True


def solve(N, L, grid):
    result = 0

    # 세로축 체크
    for x in range(N):
        if canWalk(N, L, [j[x] for j in grid]) == True:
            result += 1

    # 가로축 체크
    for y in range(N):
        if canWalk(N, L, grid[y]) == True:
            result += 1

    return result


def main():
    N, L = map(int, input().split())
    grid = []
    for _ in range(N):
        grid.append(list(map(int, input().split())))

    print(solve(N, L, grid))


main()
