# 백준 31824

'''
파랑을 왼쪽, 빨강을 오른쪽으로 모이도록 하는 경우
빨강을 왼쪽, 파랑을 오른쪽으로 모이도록 하는 경우
두 가지 경우를 모두 계산하면 된다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**8


def solve(N, ball):
    result = INF
    ballType = ['B', 'R']

    for curBall in range(2):
        # 오른쪽에서 처음 공 색이 바뀌는 곳 체크
        rightStart = None
        for i in range(N-1, -1, -1):
            if ball[i] == ballType[curBall]:
                rightStart = i
                break
        # 오른쪽 끝의 공 색을 전부 오른쪽으로 밀기
        resultA = 0
        if rightStart != None:
            for i in range(rightStart, -1, -1):
                if ball[i] == ballType[curBall^1]:
                    resultA += 1
        result = min(result, resultA)

        # 왼쪽에서 처음 공 색이 바뀌는 곳 체크
        leftStart = None
        for i in range(N):
            if ball[i] == ballType[curBall^1]:
                leftStart = i
                break
        # 왼쪽 끝의 공 색을 전부 왼쪽으로 밀기
        resultB = 0
        if leftStart != None:
            for i in range(leftStart, N):
                if ball[i] == ballType[curBall]:
                    resultB += 1
        result = min(result, resultB)

    return result


def main():
    N = int(input())
    ball = input().decode().rstrip()
    print(solve(N, ball))


main()
