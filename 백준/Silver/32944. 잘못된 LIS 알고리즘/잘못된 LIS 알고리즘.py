# 백준 32944

'''
10 4 2 -> 1 10 7 8 9 / 6 5 4 3 2
10 4 3 -> 1 2 10 8 9 / 7 6 5 4 3
10 5 3 -> 1 2 10 7 8 9 / 6 5 4 3 
10 5 4 -> 1 2 3 10 8 9 / 7 6 5 4
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve():
    if N == M:
        return [-1]

    result = [0 for _ in range(N)]
    
    num = 1
    for i in range(0, K-1):
        result[i] = num
        num += 1
    
    result[K-1] = N

    if N-1 >= M:
        for i in range(N-1, M, -1):
            result[i] = num
            num += 1
    
        for i in range(K, M+1):
            result[i] = num
            num += 1
    
    for i in range(N):
        if result[i] == 0:
            return [-1]

    return result


# main 함수 ----------
N, M, K = map(int, input().split())

print(*solve())