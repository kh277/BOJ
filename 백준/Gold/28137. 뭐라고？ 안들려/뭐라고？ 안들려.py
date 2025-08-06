# 백준 28137

'''
point[i]의 기울기가 K일 때, y절편의 값을 딕셔너리의 키로 사용한다.
그 뒤, 가능한 조합의 개수를 세면 된다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, K, point):
    slope = dict()

    for i in range(N):
        curX, curY = point[i]
        curY0 = curY - K*curX
        if curY0 in slope:
            slope[curY0] += 1
        else:
            slope[curY0] = 1
    
    result = 0
    for curY0 in slope.keys():
        result += slope[curY0]*(slope[curY0]-1)
    
    return result


def main():
    N, K = map(int, input().split())
    point = []
    for _ in range(N):
        point.append(list(map(int, input().split())))
    print(solve(N, K, point))


main()
