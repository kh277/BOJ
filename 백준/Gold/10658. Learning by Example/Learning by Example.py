# 백준 10658

import io
import math

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, A, B, data):
    data.sort()
    result = 0

    for i in range(1, N):
        prevX, prevDot = data[i-1]
        curX, curDot = data[i]
        gap = curX - prevX
        if gap & 1 == 0:
            mid = (curX + prevX) >> 1
            if A <= mid <= B and (prevDot | curDot):
                result += 1

    for i in range(N):
        left = A
        right = B

        # 왼쪽 경계 처리
        if i > 0:
            midL = (data[i-1][0] + data[i][0]) >> 1
            left = max(left, midL + 1)

        # 오른쪽 경계 처리
        if i < N-1:
            gap = data[i+1][0] - data[i][0]
            midR = (data[i][0] + data[i+1][0]) >> 1
            if gap & 1 == 0:
                right = min(right, midR - 1)
            else:
                right = min(right, midR)

        if data[i][1] == 1 and left <= right:
            result += (right - left + 1)

    return result


def main():
    N, A, B = map(int, input().split())
    data = []
    for _ in range(N):
        a, b = input().decode().split()
        if a == 'S':
            a = 1
        else:
            a = 0
        data.append((int(b), a))

    print(solve(N, A, B, data))


main()
