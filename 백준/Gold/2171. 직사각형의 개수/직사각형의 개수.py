# 백준 2171

'''
직사각형의 왼쪽 아래 점을 A, 오른쪽 아래 점을 B, 왼쪽 위 점을 C, 오른쪽 위 점을 D라고 하자.

아래 코드의 두 조건을 만족시키는 점만 따로 추출해서 저장하면 된다.
'''

import sys

input = sys.stdin.readline


def solve(N: int, points: list) -> list:
    # 좌표를 dict에 저장
    point_dict = dict()
    for i in points:
        if i[0] in point_dict:
            point_dict[i[0]].add(i[1])
        else:
            point_dict[i[0]] = {i[1]}
        
    result = 0
    
    # 좌표 2개 추출 후 직사각형 확인
    for i in range(N):
        for j in range(N):
            A = points[i]
            D = points[j]
            
            # 조건 1. A점이 왼쪽 아래, D점이 오른쪽 위에 있을 것 (즉, x, y좌표가 증가하는 순으로 놓일 것)
            # 조건 2. point_dict B, C점이 있는지 확인하기
            if A[0] < D[0] and A[1] < D[1]:
                if A[1] in point_dict[D[0]] and D[1] in point_dict[A[0]]:
                    result += 1
                    
    return result
        

def main():
    N = int(input())
    
    points = []
    for _ in range(N):
        points.append(tuple(map(int, input().split())))
    
    print(solve(N, points))


main()