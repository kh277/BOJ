# 백준 7794

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


# 선분 교차 판정 서브 함수1
def checkRange(A, B, C):
    for i in range(2):
        if not min(A[i], B[i]) <= C[i] <= max(A[i], B[i]):
            return False
    return True


# 선분 교차 판정 서브 함수2
def coef(A, B):
    if A[0] == B[0]:
        return [1, 0, A[0]]
    elif A[1] == B[1]:
        return [0, 1, A[1]]
    else:
        return [B[1]-A[1], A[0]-B[0], (B[1]-A[1])*A[0] - (B[0]-A[0])*A[1]]


# 선분 교차 판정
def lineIntetsection(A, B, C, D):
    a, b, e = coef(A, B)
    c, d, f = coef(C, D)

    det = a*d - b*c
    if det == 0:
        if e == f:
            if checkRange(A, B, C) or checkRange(A, B, D) or checkRange(C, D, A) or checkRange(C, D, B):
                if B[0] == C[0] and B[1] == C[1]:
                    return 1
                elif A[0] == D[0] and A[1] == D[1]:
                    return 1
                else:
                    return 1
            else:
                return 0
        else:
            return 0

    x = (e*d-b*f) / det
    y = (a*f-e*c) / det
    if checkRange(A, B, [x, y]) and checkRange(C, D, [x, y]):
        return 1
    else:
        return 0


def solve(A, B, pointA, pointB, cameraP):
    total = 0

    for i in range(A):
        count = 0
        for j in range(B):
            if lineIntetsection(cameraP, pointA[i], pointB[j], pointB[(j+1)%B]) == 1:
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
