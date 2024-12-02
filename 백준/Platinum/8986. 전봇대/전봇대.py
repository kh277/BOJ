# 백준 8986

'''
전봇대 사이의 거리를 x라고 두면, 전봇대들의 거리의 합은 아래로 볼록인 그래프가 된다.
따라서 삼분 탐색을 이용해 거리의 합이 최소가 되는 위치를 찾자.
'''

import sys

input = sys.stdin.readline
INF = 10e10


def check(gap):
    result = 0
    for i in range(N):
        result += abs(X[i] - gap*i)
    
    return result


def solve():
    start = 0
    end = X[-1]

    # 삼분 탐색
    while end - start >= 3:
        first = (2*start+end)//3
        second = (start+2*end)//3

        if check(first) > check(second):
            start = first
        else:
            end = second
    
    # 최종 범위에 대해 결과 도출
    result = INF
    for i in range(start, end+1):
        result = min(check(i), result)
    
    return result


# main 함수 ----------
N = int(input())
X = list(map(int, input().split()))
print(solve())