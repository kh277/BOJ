# 백준 1004

'''
(x-a)^2 + (y-b)^2 = r^2인 원의 방정식에서
점 (m, n)이 (m-a)^2 + (n-b)^2 < r^2를 만족한다면 원 내부에 존재한다고 판단할 수 있다.

원이 서로 접하는 경우는 없다고 했으니 점이 원의 내부에 있는지만 판정하면 된다.

원의 내부에 점 A, B가 둘 다 있다면 그 원은 세지 않는다.
원의 내부에 점 A만 있다면, 이탈횟수 +1을 한다.
원의 내부에 점 B만 있다면, 진입횟수 +1을 한다.
'''

import sys

input = sys.stdin.readline


def solve(start: list, end: list, circle: list) -> list:
    entry = 0
    departure = 0

    # 두 점 start, end가 원의 내부에 있는지 외부에 있는지 계산
    for a, b, r in circle:
        pos_start = r**2 - (start[0]-a)**2 - (start[1]-b)**2
        pos_end = r**2 - (end[0]-a)**2 - (end[1]-b)**2
            
        # start만 원 내부에 있다면
        if pos_start > 0 and pos_end < 0:
            departure += 1
        
        # end만 원 내부에 있다면
        elif pos_start < 0 and pos_end > 0:
            entry += 1
        
        # start, end 둘 다 원 내부에 있거나 외부에 있다면
        else:
            continue
    
    return entry + departure


def main():
    T = int(input())
    for _ in range(T):
        x1, y1, x2, y2 = map(int, input().split())

        N = int(input())

        # 원에 대한 정보를 [[c1_x, c1_y, c1_r], [c2_x, c2_y, c2_r], ...] 형태로 저장
        circle = []
        for _ in range(N):
            circle.append(map(int, input().split()))

        print(solve([x1, y1], [x2, y2], circle))


main()
