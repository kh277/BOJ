# 백준 3258

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, Z, obstacle):
    for curK in range(1, 2*N):
        curPos = 1
        while True:
            curPos += curK
            if curPos > N:
                curPos -= N

            # 장애물 체크
            if curPos in obstacle:
                break
            
            # 도착점 체크
            if curPos == Z:
                return curK

            # 무한 반복 체크
            if curPos == 1:
                break


def main():
    N, Z, M = map(int, input().split())
    obstacle = list(map(int, input().split()))

    print(solve(N, Z, obstacle))


main()
