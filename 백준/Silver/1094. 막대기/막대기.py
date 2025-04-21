# 백준 1094

'''
X를 2의 제곱수들의 합으로 나타낼 때, 사용된 제곱수의 개수를 구하는 문제이다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N):
    div = 64
    count = 0

    while N > 0:
        if div > N:
            div = div//2
            continue
        N -= div
        count += 1
    
    return count


def main():
    N = int(input())
    print(solve(N))


main()
