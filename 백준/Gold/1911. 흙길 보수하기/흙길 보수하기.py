# 백준 1911

'''
웅덩이를 정렬한 후, 작은 위치의 웅덩이부터 널판지를 덮어가며 개수 체크하기
'''

import io
from math import ceil

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, L, pool):
    pool.sort()

    prevE = -1
    count = 0
    for i in range(N):
        curS, curE = pool[i]

        # 현재 웅덩이에 널판지가 아예 없는 경우
        if prevE < curS:
            need = ceil((curE-curS+1)/L)
            count += need
            prevE = curS + need*L - 1

        # 이전 널판지가 현재 웅덩이의 일부를 덮는 경우
        elif curS <= prevE < curE:
            need = ceil((curE-prevE)/L)
            count += need
            prevE = prevE + need*L

        # 이전 널판지가 현재 웅덩이를 전부 덮는 경우
        else:
            continue

    return count


def main():
    N, L = map(int, input().split())
    pool = []
    for _ in range(N):
        a, b = map(int, input().split())
        pool.append([a, b-1])
    
    print(solve(N, L, pool))


main()
