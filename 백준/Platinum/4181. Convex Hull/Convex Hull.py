# 백준 4181

'''
Convex point을 구하는 과정 중 두 번째 단계만 완료하면 된다.
CCW를 이용하여 점들을 반시계 방향대로 정렬하자.
직선 위에 세 점이 있고 세 점 모두 Y로 들어오는 경우 세 점을 전부 출력해야 한다.

주의 반례
6
0 0 Y
1 -1 Y
2 -2 Y
4 -1 Y
5 0 Y
3 1 Y

정답
6
0 0
1 -1
2 -2
4 -1
5 0
3 1
'''

import sys
import math

input = sys.stdin.readline


# 2차원 벡터의 외적값을 이용해 회전 방향 판별
def CCW(a, b, c):
    # 양수(반시계), 0(일직선), 음수(시계)
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


# Convex Hull 구하기
def convex_hull(graph):
    # x좌표 오름차순으로 정렬
    graph = sorted(set(graph))

    # 아래쪽 Hull을 구함
    lower = []
    for i in graph:
        # 반시계 방향이 아닐 경우 마지막 점 제거
        while len(lower) >= 2 and CCW(lower[-2], lower[-1], i) < 0:
            lower.pop()
        lower.append(i)
        
    # 위쪽 Hull을 구함
    upper = []
    for i in reversed(graph):
        # 반시계 방향이 아닐 경우 마지막 점 제거
        while len(upper) >= 2 and CCW(upper[-2], upper[-1], i) < 0:
            upper.pop()
        upper.append(i)
    
    # 아래쪽 Hull과 위쪽 Hull을 중복제거하여 합치기
    return lower[:-1] + upper[:-1]


def solve(points: list) -> list:

    # 볼록 껍질을 이루는 점 구하기
    result = convex_hull(points)

    # x좌표의 최소값을 제일 앞에 오도록 재배치하기
    min = [10e10, 10e10, 10e10]
    for i in range(len(result)):
        if result[i][0] <= min[0]:
            if result[i][1] < min[1]:
                min = [result[i][0], result[i][1], i]
    
    return [len(result)] + result[min[2]:] + result[:min[2]]


def main():
    N = int(input())

    points = []
    for i in range(N):
        a, b, c = input().split()
        points.append((int(a), int(b)))
    
    # 결과 출력
    result = solve(points)
    print(result[0])
    for i in range(1, result[0]+1):
        print(*result[i])


main()