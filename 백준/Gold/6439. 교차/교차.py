# 백준 6439

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


def solve(lineS, lineE, sqS, sqE):
    A = (sqS[0], sqS[1])
    B = (sqS[0], sqE[1])
    C = (sqE[0], sqS[1])
    D = (sqE[0], sqE[1])

    # 두 점이 사각형 내부에 있는 경우 체크
    if sqS[0] <= lineS[0] <= sqE[0] and sqS[1] <= lineS[1] <= sqE[1]:
        return True
    if sqS[0] <= lineE[0] <= sqE[0] and sqS[1] <= lineE[1] <= sqE[1]:
        return True

    # 직사각형의 각 변과 교차하는지 체크
    return LineIntersection(lineS, lineE, A, B) | LineIntersection(lineS, lineE, A, C) | LineIntersection(lineS, lineE, B, D) | LineIntersection(lineS, lineE, C, D)


def main():
    T = int(input())
    for _ in range(T):
        a, b, c, d, e, f, g, h = map(int, input().split())
        print('F' if solve((a, b), (c, d), (min(e, g), min(f, h)), (max(e, g), max(f, h))) == False else 'T')


main()
