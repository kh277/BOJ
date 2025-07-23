# 백준 6600

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
PI = 3.141592653589793


def distance(A, B):
    return ((A[0]-B[0])**2 + (A[1]-B[1])**2)**0.5


def solve(A, B, C):
    a = distance(B, C)
    b = distance(C, A)
    c = distance(A, B)
    cosA = (b*b + c*c - a*a) / (2*b*c)
    sinA = (1 - cosA*cosA)**0.5

    return round(PI * a / sinA, 2)


def main():
    while True:
        try:
            x1, y1, x2, y2, x3, y3 = map(float, input().split())
            print(solve([x1, y1], [x2, y2], [x3, y3]))
        except:
            break


main()
