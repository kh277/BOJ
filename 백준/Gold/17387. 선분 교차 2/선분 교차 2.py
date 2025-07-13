# 백준 17387

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


def main():
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())
    print(0 if LineIntersection((x1, y1), (x2, y2), (x3, y3), (x4, y4)) == False else 1)


main()
