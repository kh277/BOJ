# 백준 25339

'''
두 수의 위치를 변경하면 2로 나눈 나머지가 변한다.
구간을 뒤집을 때, 뒤집히는 수가 홀수개이면 2로 나눈 나머지가 변한다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def main():
    N, Q = map(int, input().split())
    curRes = 0
    for _ in range(Q):
        a, l, r = map(int, input().split())
        if a == 1:
            curRes ^= 1
        elif a == 2 and ((r-l+1)//2) % 2 == 1:
            curRes ^= 1
        print(curRes)


main()
