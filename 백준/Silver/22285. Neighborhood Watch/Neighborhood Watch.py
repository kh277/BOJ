# 백준 22285

'''
A_i = 구간 (i번째 WH의 위치, i+1번째 WH의 위치]에 있는 집,
B_i = 구간 [i번째 WH의 위치, N번째 집]에 있는 집이라고 할 때,
전체 경우의 수는 A_1*B_1 + A_2*B_2 + ...가 된다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve():
    if K == 0:
        return 0

    result = 0

    # 첫 watchHouse에 대해 처리
    left = watchHouse[0]
    right = N - watchHouse[0] + 1
    result += left*right

    for curPos in range(1, K):
        left = watchHouse[curPos] - watchHouse[curPos-1]
        right = N - watchHouse[curPos] + 1

        result += left*right

    return result


# main 함수 ----------
N, K = map(int, input().split())
watchHouse = []
for _ in range(K):
    watchHouse.append(int(input()))

print(solve())
