# 백준 4134

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def modPow(base, exp, MOD):
    result = 1
    while exp:
        if exp & 1:
            result = (result*base) % MOD
        base = (base*base) % MOD
        exp >>= 1

    return result


def MillerRabin(num, base):
    if num % base == 0:
        return True if num != base else False

    exp = num-1
    while True:
        temp = modPow(base, exp, num)
        if exp & 1:
            return True if temp != 1 and temp != num-1 else False
        elif temp == num-1:
            return False
        exp >>= 1


# 밀러-라빈 소수판별법
def isPrime(num):
    base = [2, 3, 5, 7, 11]
    maxBase = base[-1]
    if num <= maxBase:
        if num in base:
            return True
        return False

    for i in base:
        if num == i:
            return True
        if MillerRabin(num, i) == True:
            return False
    if num <= maxBase:
        return False

    return True


def solve(N):
    cur = N
    while True:
        if isPrime(cur) == True:
            return cur
        cur += 1


def main():
    T = int(input())
    for _ in range(T):
        print(solve(int(input())))


main()
