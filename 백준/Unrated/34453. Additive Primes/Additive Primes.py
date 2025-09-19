# 백준 34453

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


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


def solve(N):
    total = sum([int(i) for i in str(N)])
    if isPrime(N) == False:
        return "COMPOSITE"
    elif isPrime(total) == False:
        return "PRIME, BUT NOT ADDITIVE"
    else:
        return "ADDITIVE PRIME"


def main():
    N = int(input())
    print(solve(N))


main()
