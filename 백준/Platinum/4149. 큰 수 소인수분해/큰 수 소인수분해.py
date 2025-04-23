# 백준 4149

import io
from random import randrange
from math import gcd

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
        return False

    exp = num-1
    while True:
        temp = modPow(base, exp, num)
        if exp & 1:
            return True if temp != 1 and temp != num-1 else False
        elif temp == num-1:
            return False
        exp >>= 1


def isPrime(num):
    testFull = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for i in testFull:
        if num == i:
            return True
        if num > 40 and MillerRabin(num, i) == True:
            return False
    if num <= 40:
        return False

    return True


def f(x, mod, c):
    return ((x*x)%mod + c) % mod


def cycle(num, factor):
    if num == 1:
        return

    if num % 2 == 0:
        factor.append(2)
        cycle(num//2, factor)
        return

    if isPrime(num) == True:
        factor.append(num)
        return

    while True:
        x = randrange(2, num)
        y = x
        c = randrange(1, num)
        d = 1

        while d == 1:
            x = f(x, num, c)
            y = f(f(y, num, c), num, c)
            d = gcd(abs(x-y), num)

        if d == num:
            continue

        break

    cycle(d, factor)
    cycle(num//d, factor)


def PollardRho(num):
    factor = []
    cycle(num, factor)

    return sorted(factor)


def main():
    N = int(input())
    for i in PollardRho(N):
        print(i)


main()
