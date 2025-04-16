# 백준 14247

'''
나무가 자라는 길이가 작은 것부터 베면 된다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, H, A):
    data = [[A[i], H[i]] for i in range(N)]
    data.sort(key= lambda x: (x[0]))

    result = 0
    for i in range(N):
        result += data[i][0]*i + data[i][1]

    return result


def main():
    N = int(input())
    data = []
    H = list(map(int, input().split()))
    A = list(map(int, input().split()))
    print(solve(N, H, A))


main()
