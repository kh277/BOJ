# 백준 3387

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N):
    for i in [10, 16, 25]:
        if N % i == 0:
            return ['Impossible']

    canMake = []
    for i in range(1, 1000):
        for j in range(1, 10):
            canMake.append(int(str(j)*i))

    for i in canMake:
        if i % N == 0:
            return [str(i)[0], len(str(i))]
    
    return ['Impossible']


# main 함수 ----------
N = int(input())

print(*solve(N))
