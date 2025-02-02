# 백준 13011

'''
C[i] * 밀도 = W[i]이고, 실제로 받은 무게와의 차이는 브루트포스로 구하면 된다.
(밀도)값에 따라 (실제로 받은 무게와의 차이)의 값이 감소 -> 증가하는 그래프가 형성되므로
삼분 탐색으로 최적값을 찾으면 된다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def check(density):
    result = 0
    for i in range(N):
        result += abs(W[i] - (C[i] * density))
    
    return result


def solve():
    start = 0
    end = 100000000

    count = 0
    while count < 200:
        mid1 = (start*2+end)/3
        mid2 = (start+end*2)/3

        if check(mid1) > check(mid2):
            start = mid1
        else:
            end = mid2

        count += 1

    return check((mid1+mid2)/2)


# main 함수 ----------
N = int(input())
C = list(map(int, input().split()))
W = list(map(int, input().split()))
print(solve())