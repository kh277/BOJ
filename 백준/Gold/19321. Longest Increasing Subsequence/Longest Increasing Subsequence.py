# 백준 19321

'''
15403번과 거의 유사하다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, A):
    LIS = [[] for _ in range(N+1)]
    for i in range(N):
        LIS[A[i]].append(i)

    result = [0 for _ in range(N)]
    count = 1
    for i in range(N+1):
        for j in LIS[i][::-1]:
            result[j] = count
            count += 1

    return result


def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(*solve(N, A))


main()
