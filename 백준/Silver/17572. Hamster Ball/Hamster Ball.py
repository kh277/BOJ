# 백준 17572

import io
import math

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(T, B, ball):
    ball.sort(key= lambda x: (x[1], x[0]))

    leftL = T
    result = 0
    for i in range(B):
        count, r = ball[i]
        size = 2*r*math.pi

        # 제한 체크
        if size*count <= leftL:
            leftL -= size*count
            result += count
        else:
            result += int(leftL/size)
            break
    
    return result


def main():
    T = int(input())
    B = int(input())
    ball = []
    for _ in range(B):
        ball.append(list(map(int, input().split())))
    
    print(solve(T, B, ball))


main()
