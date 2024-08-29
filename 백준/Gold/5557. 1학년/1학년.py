# 백준 5557

'''
DP 테이블의 가로축은 0~20까지의 수, 세로축은 주어진 숫자의 인덱스(j)이다.
예제1에서
0번째 인덱스 수 8은 초기값으로 DP[0][8] = 1을 저장한다
1번째 인덱스 수 3은 0~20의 값 i에 대해 DP[1][i] = DP[0][i-3] + DP[0][i+3]의 값을 저장한다.
이 과정을 N-2번째 인덱스 수까지 반복한 뒤, DP[N-2][num[N-1]]의 값을 찾으면 된다. 
'''

import sys

input = sys.stdin.readline


def solve(N: int, num: list) -> int:
    DP = [[0 for _ in range(21)] for _ in range(N-1)]
    
    # 초기값
    DP[0][num[0]] = 1   # num[0]번째 수만을 이용해 num[0]을 만드는 경우의 수 1가지

    for i in range(1, N-1):
        for j in range(21):
            if j-num[i] >= 0:
                DP[i][j] += DP[i-1][j-num[i]]
            if j+num[i] <= 20:
                DP[i][j] += DP[i-1][j+num[i]]
    
    return DP[N-2][num[N-1]]


def main():
    N = int(input())
    num = list(map(int, input().split()))

    print(solve(N, num))


main()