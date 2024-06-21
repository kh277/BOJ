# 백준 17386

'''
17387 코드와 동일
'''

import sys

input = sys.stdin.readline


# 이차원 좌표 A, B 사이에 check값이 존재하는지 확인
def check_range(A: list, B: list, check: list) -> bool:
    # 정의역과 치역에 대해 확인
    for i in range(2):
        if not min(A[i], B[i]) <= check[i] <= max(A[i], B[i]):
            return False
    
    return True


# 두 점 A, B를 입력받아 ax + by = c의 계수 a, b, c를 리턴하는 함수
def coef(A: list, B: list) -> list:
    if A[0] == B[0]:
        return [1, 0, A[0]]
    elif A[1] == B[1]:
        return [0, 1, A[1]]
    else:
        return [B[1]-A[1], A[0]-B[0],  (B[1]-A[1])*A[0] - (B[0]-A[0])*A[1]]


# 크래머 공식을 이용하여 선분 교차 판정
def line_segment_intetsection(A: list, B: list, C: list, D: list) -> int:
    # ax + by = e, cx + dy = f 꼴의 연립일차방정식 도출
    a, b, e = coef(A, B)
    c, d, f = coef(C, D)

    # 도출한 연립일차방정식의 해 판정
    det = a*d - b*c

    # 해가 없거나 무수히 많은 경우
    if det == 0:
        # 두 선분이 일치하는 경우
        if e == f:
            # 두 선분의 정의역이 겹치면 교차 판정
            if check_range(A, B, C) or check_range(A, B, D) or check_range(C, D, A) or check_range(C, D, B):
                return 1
            else:
                return 0
        
        # 두 선분이 평행하는 경우
        else:
            return 0

    # 해가 존재하는 경우
    x = (e*d-b*f) / det
    y = (a*f-e*c) / det

    # 해가 선분 위에 존재하는지 확인
    if check_range(A, B, [x, y]) and check_range(C, D, [x, y]):
        return 1
    else:
        return 0
            

def main():
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())

    print(line_segment_intetsection([x1, y1], [x2, y2], [x3, y3], [x4, y4]))


main()