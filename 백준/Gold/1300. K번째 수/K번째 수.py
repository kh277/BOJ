# 백준 1300

'''
생각의 흐름
1. N*N 크기의 이차원 배열을 정렬하면 N^2logN 만큼의 시간이 걸리므로 더 효율적으로 해결해야 한다.
2. B[K] = R라고 하면, R와 같거나 작은 수가 최소 K개 존재한다.

결정 문제 : B에서 x 이하인 수가 최소 K개 존재하는가?
'''

import sys

input = sys.stdin.readline


# B에서 x 이하인 수의 개수 세기
def check(x: int):
    result = 0
    
    for i in range(1, N+1):
        temp = min(x//i, N)
        if temp == 0:
            break
        else:
            result += temp

    return result


def solve():
    start = 1
    end = N*N
    
    while True:
        # 탈출조건
        if end - start <= 1:
            if check(start) < K:
                return end
            else:
                return start
        
        mid = (start+end)//2
        
        # 결정 문제 확인
        cur = check(mid)
        
        # 이분 탐색
        if cur < K:
            start = mid
        else:
            end = mid
    

# main 함수 ----------
N = int(input())
K = int(input())

print(solve())
