# 백준 2254

'''
N개의 점에서 볼록 껍질을 만들고 그 점들을 P_i로 저장한다.
이후 다시 볼록 껍질을 만들고 그 점들을 P_(i+1)로 저장한다.
...
위 과정에서 가장 바깥쪽 껍질 내에 감옥이 있는지 판단한다.
'''

import sys

# 2차원 벡터의 외적값을 이용해 회전 방향 판별
def CCW(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


# graph에 있는 점에서 Convex Hull 구하기
def convex_hull(graph):
    graph = sorted(set(graph))

    lower = []
    for i in graph:
        while len(lower) >= 2 and CCW(lower[-2], lower[-1], i) <= 0:
            lower.pop()
        lower.append(i)
        
    upper = []
    for i in reversed(graph):
        while len(upper) >= 2 and CCW(upper[-2], upper[-1], i) <= 0:
            upper.pop()
        upper.append(i)
    
    return lower[:-1] + upper[:-1]


# hull 내부에 point가 있는지 확인
def point_in_polygon(point, hull):
    if CCW(hull[0], hull[-1], point) > 0:
        return False
    if CCW(hull[0], hull[1], point) < 0:
        return False

    left = 1
    right = len(hull) - 1
    while left < right:
        mid = (left + right) // 2
        if CCW(hull[0], hull[mid], point) > 0:
            left = mid + 1
        else:
            right = mid

    return CCW(hull[left-1], hull[left], point) > 0


def solve():
    result = 0
    leftPoint = point
    
    # 점이 남지 않을 때까지 반복
    while True:
        if len(leftPoint) < 3:
            break
        
        # leftPoint로 Convex Hull 구하기
        hull = convex_hull(leftPoint)
        
        # hull 내부에 감옥이 있는지 확인
        if point_in_polygon((pX, pY), hull) == True:
            result += 1
        else:
            break
        
        # hull에 사용된 점 제거
        leftPoint = list(set(leftPoint) - set(hull))
    
    return result


# main 함수 ----------
N, pX, pY = map(int, input().split())

point = []
for _ in range(N):
    point.append(tuple(map(int, input().split())))

print(solve())