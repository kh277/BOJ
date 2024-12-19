# 백준 31739

'''
우정이의 시작 지점은 무조건 모기가 존재하는 위치에서 시작하는 것이 이득이다.
모든 모기 위치에 대해 시작점을 잡고, 백트래킹으로 각 경우에 대해 최대값을 구하면 된다.

아름이 역시 모든 좌표에 대해 최대값을 구하면 된다.
'''

import io

input = io.BufferedReader(io.FileIO(0)).readline


# curIndex번째 모기의 위치에서 nextIndex번째 모기의 위치로 이동할 수 있는지 체크
def promising(curIndex, nextIndex, visited, accMove):
    # 이미 방문했는지 체크
    if nextIndex in visited:
        return False

    curY, curX, _ = mosquito[curIndex]
    nextY, nextX, _ = mosquito[nextIndex]

    # 다음 좌표까지 움직일 수 있는지 체크
    if accMove + abs(curY-nextY) + abs(curX-nextX) > T:
        return False
    
    return True


# 백트래킹으로 모기를 최대 몇마리까지 잡을 수 있는지 체크
def backtrack(curIndex, visited, accMove):
    # 종료조건
    if len(visited) == K:
        return len(visited)
    
    # 유망성 판단
    result = 0
    for i in range(K):
        if promising(curIndex, i, visited, accMove) == True:
            curY, curX, _ = mosquito[curIndex]
            nextY, nextX, _ = mosquito[i]
            result = max(result, backtrack(i, visited | {i}, accMove+abs(curY-nextY)+abs(curX-nextX)))
    
    return max(len(visited), result)


# coreY, coreX 위치를 중심으로 전기장이 형성될 때, 잡을 수 있는 모기의 수 체크
def checkMoskito(coreY, coreX):
    count = 0
    for i in range(K):
        mosY, mosX, mosHp = mosquito[i]
        distL = abs(coreY-mosY)+abs(coreX-mosX)

        # 중심에 모기가 존재한다면
        if distL == 0:
            force = 40
        else:
            force = P/distL

        if mosHp <= force:
            count += 1
    
    return count


# 브루트포스로 core의 위치를 전부 탐색하여 잡을 수 있는 모기의 최대값 산출
def bruteforce():
    catchCount = 0
    for y in range(N):
        for x in range(M):
            catchCount = max(catchCount, checkMoskito(y, x))
    
    return catchCount


def solve():
    # 우정이가 잡을 수 있는 모기의 수 계산
    countA = 0
    for startIndex in range(K):
        countA = max(countA, backtrack(startIndex, {startIndex}, 0))
    
    # 아름이가 잡을 수 있는 모기의 수 계산
    countB = bruteforce()
    
    return [countA, countB]


# main 함수 ----------
N, M, K, T, P = map(int, input().split())
grid = [[[] for _ in range(M)] for _ in range(N)]
mosquito = []
for _ in range(K):
    y, x, hp = map(int, input().split())
    mosquito.append([y-1, x-1, hp])
    grid[y-1][x-1].append(hp)

print(*solve())