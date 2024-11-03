# 백준 18234

'''
N종류의 당근을 T일동안 키운다.
첫 번째 당근의 t일차 맛은 w_1 + p_(t-1)이다.
두 번째 당근의 t일차 맛은 w_2 + p_(t-2)이다.

또한 당근이 심어져 있지 않으면 심어야 하므로 당근을 계속해서 먹을 경우 손해가 나게 된다.
따라서 p가 큰 값일 수록 나중에 먹고, 1 ~ T-N일차까지는 당근을 먹지 않는 것이 이득이다. 
'''

import sys

input = sys.stdin.readline

def solve():
    carrot.sort(key= lambda x: (-x[1], -x[0]))

    result = 0
    day = T
    for carrotNum in range(N):
        result += carrot[carrotNum][0] + carrot[carrotNum][1] * (day-1)
        day -= 1

    return result


# main 함수 ----------
N, T = map(int, input().split())

carrot = []
for _ in range(N):
    carrot.append(list(map(int, input().split())))

print(solve())