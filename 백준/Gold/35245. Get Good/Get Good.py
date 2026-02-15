# 백준 35245

'''
(지친 상태에서 y일 휴식 + 회복 후 최상의 상태로 x일동안 a만큼의 숙련도)를 한 사이클로 볼 수 있다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, a, b, x, y):
    # 초기 최상의 컨디션으로 일정이 끝나는 경우
    if N <= x:
        return a*N

    result = a*x
    N -= x

    # 휴식을 취하지 않는 것이 더 이득일 경우
    if a*x <= b*(x+y):
        return result + b*N

    # 필요한 사이클 횟수 반복
    cycle = N // (x+y)
    result += cycle*a*x
    
    # 남은 일자동안 휴식을 취하고 최상의 컨디션으로 일할지, 지친 상태로 일할지 판단
    N -= cycle*(x+y)
    if N <= y:
        return result + N*b
    return result + max((N-y)*a, N*b)


def main():
    T = int(input())
    for _ in range(T):
        N, a, b, x, y = map(int, input().split())
        print(solve(N, a, b, x, y))


main()
