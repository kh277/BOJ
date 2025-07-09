# 백준 19939

'''
일단 모든 바구니에 1, 2, ..., K개의 공을 분배한다.
그 뒤, 모든 바구니에 동일한 개수의 공을 최대한 분배한다.
남은 공이 0개라면, 공의 개수 차이는 K-1이 된다.
남은 공이 구간 [1, K-1]에 속한다면, K번째 바구니에 +1, K-1번째 바구니에 +1, ... 을 진행하면 된다.
이 경우 공의 개수 차이는 K가 된다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, K):
    # 모든 바구니에 오름차순 분배
    if K*(K+1)//2 > N:
        return -1
    leftBall = N - K*(K+1)//2

    # 모든 바구니에 동일한 개수 분배
    leftBall %= K

    # 남은 값에 따라 분배
    if leftBall == 0:
        return K-1
    else:
        return K


def main():
    N, K = map(int, input().split())
    print(solve(N, K))


main()
