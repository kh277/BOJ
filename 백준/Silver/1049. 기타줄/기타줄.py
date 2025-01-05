# 백준 1049

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve():
    six.sort()
    one.sort()

    return min(six[0]*(N//6)+one[0]*(N%6), six[0]*(N//6+1), one[0]*N)


# main 함수 ----------
N, M = map(int, input().split())
six = []
one = []
for _ in range(M):
    a, b = list(map(int, input().split()))
    six.append(a)
    one.append(b)

print(solve())