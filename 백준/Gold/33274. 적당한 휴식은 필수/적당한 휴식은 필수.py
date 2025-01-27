# C번

'''
행의 총합, 열의 총합이 같게 되어야 한다.
따라서 짝수일 경우, 0 ~ 2N-1까지의 수를 적절하게 분배하면 된다. ex) [0, 1, 6, 7], [2, 3, 4, 5]
홀수일 경우는 0 ~ 2N-2까지의 수를 적절하게 분배하면 된다. ex) [0, 1, 2, 8, x], [3, 4, 5, 6, 7]

4 -> 행 [0, 1, 6, 7], [2, 3, 4, 5]
0 1 1 0 
0 0 3 0
0 0 2 2
0 0 0 5

5 -> sumX[0, 1, 2, 8, x], sumY[3, 4, 5, 6, 7]
0 1 2 0 0
0 0 0 4 0
0 0 0 4 1
0 0 0 0 6
0 0 0 0 7
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve():
    if N == 1:
        return [[0]]

    grid = [[0 for _ in range(N)] for _ in range(N)]

    # 짝수일 때
    if N % 2 == 0:
        sumX = []
        sumY = []

        num = 0
        for _ in range(N//2):
            sumX.append(num)
            num += 1
        for _ in range(N):
            sumY.append(num)
            num += 1
        for _ in range(N//2):
            sumX.append(num)
            num += 1
        
        canUse = sumY[:]
        for x in range(1, N):
            curSum = sumX[x]
            for y in range(N):
                if curSum == 0:
                    break

                if curSum > canUse[y]:
                    curSum -= canUse[y]
                    grid[y][x] += canUse[y]
                    canUse[y] = 0
                else:
                    grid[y][x] += curSum
                    canUse[y] -= curSum
                    curSum = 0
    
    # 홀수일 때
    else:
        sumX = []
        sumY = []

        num = 0
        for _ in range(N//2+1):
            sumX.append(num)
            num += 1
        for _ in range(N):
            sumY.append(num)
            num += 1
        for _ in range(N//2):
            sumX.append(num)
            num += 1

        canUse = sumY[:]
        for x in range(1, N):
            curSum = sumX[x]
            for y in range(N):
                if curSum == 0:
                    break

                if curSum > canUse[y]:
                    curSum -= canUse[y]
                    grid[y][x] += canUse[y]
                    canUse[y] = 0
                else:
                    grid[y][x] += curSum
                    canUse[y] -= curSum
                    curSum = 0

        grid[N-1][N-1] += canUse[N-1]

    return grid


# main 함수 ----------
N = int(input())
for i in solve():
    print(*i)