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
    if N % 2 != 0 and N % 3 != 0 and N % 5 != 0 and N % 7 != 0:
        return -1
    

    while True:
        if N % 8 == 0:
            N = N//8
            result += 1
        elif N % 4 == 0:
            N = N//4
            result += 1
        elif N % 6 == 0:
            N = N//6
            result += 1
        elif N % 9 == 0:
            N = N//9
            result += 1
        else:
            if N % 2 == 0:
                N = N//2
                result += 1
            elif N % 3 == 0:
                N = N//3
                result += 1
            elif N % 5 == 0:
                N = N//5
                result += 1
            elif N % 7 == 0:
                N = N//7
                result += 1
            else:
                if N != 1:
                    return -1
                break
    
    return result


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(solve(N))


main()
