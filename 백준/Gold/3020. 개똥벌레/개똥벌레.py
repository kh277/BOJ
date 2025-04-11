# 백준 3020

'''
top, bottom의 i번째 인덱스는 높이가 i일 때 종유석, 석순의 개수이다.
따라서 높이가 i일 때 장애물은 top[i] + bottom[i]가 된다.
'''

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 500001


def solve(H, top, bottom):
    # 높이 누적 합 계산
    for i in range(H-1, 0, -1):
        bottom[i] += bottom[i+1]
        top[i] += top[i+1]

    # 종유석의 높이 뒤집기
    top[1:H+1] = top[H:0:-1]

    # 최소값 도출
    result = [INF, 0]
    for i in range(1, H+1):
        curBreak = top[i] + bottom[i]
        if result[0] > curBreak:
            result = [curBreak, 1]
        elif result[0] == curBreak:
            result[1] += 1

    return result


def main():
    N, H = map(int, input().split())
    top = array('I', [0]*(H+1))
    bottom = array('I', [0]*(H+1))
    for i in range(N):
        if i % 2 == 0:
            bottom[int(input())] += 1
        else:
            top[int(input())] += 1

    print(*solve(H, top, bottom))


main()
