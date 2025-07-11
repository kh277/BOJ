# 백준 3089

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
ARRAY_TYPE = 'i'
MOVE = {'U': 1, 'D': -1, 'L': -1, 'R': 1}


# arr에서 target 이상인 첫 번째 요소의 인덱스 반환
def LowerBound(arr, target):
    start = 0
    end = len(arr)

    while start < end:
        mid = (start+end)//2
        if arr[mid] < target:
            start = mid+1
        else:
            end = mid

    return start


def solve(N, M, xClover, yClover, command):
    for i in xClover.keys():
        xClover[i] = sorted(xClover[i])
    for i in yClover.keys():
        yClover[i] = sorted(yClover[i])

    # 각 커맨드에 대해 저장된 좌표에서 이분 탐색으로 다음 지점 탐색
    curX = 0
    curY = 0
    for i in range(M):
        curC = command[i]
        if curC == 'U' or curC == 'D':
            curY = xClover[curX][LowerBound(xClover[curX], curY)+MOVE[curC]]
        else:
            curX = yClover[curY][LowerBound(yClover[curY], curX)+MOVE[curC]]

    return [curX, curY]


def main():
    N, M = map(int, input().split())

    # xClover[i] = x=i인 점들의 y좌표 저장
    xClover = dict()
    yClover = dict()
    for _ in range(N):
        x, y = map(int, input().split())
        if x not in xClover:
            xClover[x] = array(ARRAY_TYPE, [y])
        else:
            xClover[x].append(y)
        if y not in yClover:
            yClover[y] = array(ARRAY_TYPE, [x])
        else:
            yClover[y].append(x)
    command = input().decode().rstrip()
    print(*solve(N, M, xClover, yClover, command))


main()
