# 백준 9334

'''
특이 케이스 :
8 0 0 1 0 0 3 0 0   -> 9
9 0 1 0 3 0 9 0 27 0   -> 81
'''

import sys

input = sys.stdin.readline


def case_1(L: list) -> list:
    # 1. 해 구하기
    # f(2) = af(1)를 만족하는 a 찾기
    if L[1] == 0 and L[2] == 0:
        x = L[4] / L[3]
    elif L[2] == 0:
        x = L[2] / L[1]
    elif L[1] == 0:
        x = L[3] / L[2]
    else:
        x = L[2] / L[1]
    
    # 2. 이후 수에 대해 검사. 예외 발견 시 다음 케이스로
    for i in range(2, L[0]):
        if L[i] != x*L[i-1]:
            return [False, -1]
    
    return [True, int(x*L[L[0]])]


def case_2(L: list) -> list:
    # 1. 해 구하기
    # f(3) = af(2)+bf(1)
    # f(4) = af(3)+bf(2)를 만족하는 a, b 찾기

    D = L[2]*L[2] - L[1]*L[3]
    Dx = L[3]*L[2] - L[1]*L[4]
    Dy = L[2]*L[4] - L[3]*L[3]
    
    # 해가 무수히 많거나, 없는 경우
    if D == 0:
        return [False, None]
    
    x = Dx / D
    y = Dy / D
    
    # 2. 이후 수에 대해 검사. 예외 발견 시 다음 케이스로
    for i in range(3, L[0]):
        if L[i] != x*L[i-1] + y*L[i-2]:
            return [False, None]
    
    return [True, int(x*L[L[0]] + y*L[L[0]-1])]


def determinant_3x3(matrix):
    return (matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) -
            matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]) +
            matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]))


def case_3(L: list) -> list:
    # 1. 해 구하기
    # f(4) = af(3)+bf(2)+cf(1)
    # f(5) = af(4)+bf(3)+cf(2)
    # f(6) = af(5)+bf(4)+cf(3)를 만족하는 a, b, c 찾기
    A = [[L[3], L[2], L[1]], [L[4], L[3], L[2]], [L[5], L[4], L[3]]]
    b = [L[4], L[5], L[6]]

    Dx = determinant_3x3([[b[0], A[0][1], A[0][2]], [b[1], A[1][1], A[1][2]], [b[2], A[2][1], A[2][2]]])
    Dy = determinant_3x3([[A[0][0], b[0], A[0][2]], [A[1][0], b[1], A[1][2]], [A[2][0], b[2], A[2][2]]])
    Dz = determinant_3x3([[A[0][0], A[0][1], b[0]], [A[1][0], A[1][1], b[1]], [A[2][0], A[2][1], b[2]]])
    x = Dx / determinant_3x3(A)
    y = Dy / determinant_3x3(A)
    z = Dz / determinant_3x3(A)

    # 2. 적어도 하나의 식을 만족하는 입력만 들어오므로
    # 이후 입력에 대해 체크할 필요가 없다.
    # 마지막 값만 출력하면 된다.

    return [True, int(x*L[L[0]] + y*L[L[0]-1] + z*L[L[0]-2])]


def solve(L: list) -> int:
    # 첫 번쨰 케이스 : f(n) = af(n-1) 꼴
    temp = case_1(L)
    if temp[0]:
        return temp[1]
    
    # 두 번째 케이스 : f(n) = af(n-1) + bf(n-2) 꼴
    temp = case_2(L)
    if temp[0]:
        return temp[1]
    
    # 세 번째 케이스 : f(n) = af(n-1) + bf(n-2) + cf(n-3) 꼴
    temp = case_3(L)
    if temp[0]:
        return temp[1]


def main():
    T = int(input())

    for _ in range(T):
        L = list(map(int, input().split()))
        
        print(solve(L))

main()