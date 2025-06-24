# 백준 11758

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def CCW(A, B, C):
    result = A[0]*B[1] + B[0]*C[1] + C[0]*A[1]
    result -= B[0]*A[1] + C[0]*B[1] + A[0]*C[1]
    return (result > 0) - (result < 0)


def main():
    point = []
    for i in range(3):
        point.append(list(map(int, input().split())))
    
    print(CCW(point[0], point[1], point[2]))


main()