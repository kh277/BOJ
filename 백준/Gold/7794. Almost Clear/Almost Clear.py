# 백준 7794

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


# 선분 교차 판정 서브 함수
def CCW(A, B, C):
    return (B[0]-A[0]) * (C[1]-A[1]) - (B[1]-A[1]) * (C[0]-A[0])


# 선분 교차 판정
def LineIntersection(A, B, C, D):
    AB = CCW(A, B, C) * CCW(A, B, D)
    CD = CCW(C, D, A) * CCW(C, D, B)

    if AB == 0 and CD == 0:
        if B < A:
            A, B = B, A
        if D < C:
            C, D = D, C
        return not (B < C or D < A)

    return AB <= 0 and CD <= 0


def solve(A, B, pointA, pointB, cameraP):
    total = 0

    for i in range(A):
        count = 0
        for j in range(B):
            if LineIntersection(cameraP, pointA[i], pointB[j], pointB[(j+1)%B]) == 1:
                count += 1
                break
        if count > 0:
            total += 1

    if total == 0:
        return "CLEAR"
    elif total == A:
        return "NO VISION"
    return "ALMOST CLEAR"


def main():
    T = int(input())
    for _ in range(T):
        temp = list(map(int, input().split()))
        A = temp[0]
        pointA = [(temp[i], temp[i+1]) for i in range(1, A*2, 2)]
        temp = list(map(int, input().split()))
        B = temp[0]
        pointB = [(temp[i], temp[i+1]) for i in range(1, B*2, 2)]
        cameraP = tuple(map(int, input().split()))

        print(solve(A, B, pointA, pointB, cameraP))


main()
