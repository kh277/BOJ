# 백준 15810

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def check(N, time, A):
    count = 0
    for i in range(N):
        count += time//A[i]
    return count


def solve(N):
    result = 0
    if len(str(N)) == 1:
        return 1

    while True:
        flag = False
        for i in [8, 4, 6, 9, 2, 3, 5, 7]:
            if N % i == 0:
                N = N//i
                result += 1
                flag = True
                break
        
        if flag == False:
            if N == 1:
                return result
            else:
                return -1


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(solve(N))


main()
