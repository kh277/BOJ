# 백준 2023

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
prime = []


def isPrime(N):
    if N <= 1:
        return False
    elif N <= 3:
        return True
    elif N % 2 == 0 or N % 3 == 0:
        return False

    for i in range(5, int(N**0.5)+1, 6):
        if N % i == 0 or N % (i + 2) == 0:
            return False

    return True


def recur(depth, curNum):
    if depth == 1:
        prime.append(curNum)
        return
    
    for i in [1, 3, 5, 7, 9]:
        nextNum = curNum*10 + i
        if isPrime(nextNum) == True:
            recur(depth-1, nextNum)
    
    return


def solve(N):
    for i in [2, 3, 5, 7]:
        recur(N, i)
    
    return list(prime)


def main():
    N = int(input())
    for i in solve(N):
        print(i)


main()
