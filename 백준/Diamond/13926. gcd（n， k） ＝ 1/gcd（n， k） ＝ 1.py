# 백준 13926

'''
팀노트를 참고해서 작성했음
'''

from random import randrange
from math import gcd


# 밀러-라빈 파츠1
def modPow(base, exp, MOD):
    result = 1
    while exp:
        if exp & 1:
            result = (result*base) % MOD
        base = (base*base) % MOD
        exp >>= 1

    return result


# 밀러-라빈 파츠2
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


# 밀러-라빈 소수판별법
def isPrime(num):
    for i in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
        if num == i:
            return True
        if num > 40 and MillerRabin(num, i) == True:
            return False
    if num <= 40:
        return False

    return True


# 폴라드-로 파츠1
def f(x, mod, c):
    return ((x*x)%mod + c) % mod


# 폴라드-로 파츠2
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


# 폴라드 로
def PollardRho(num):
    factor = []
    cycle(num, factor)

    return sorted(factor)


# 오일러 피 함수
def EularPhi(num):
    # 인수 중복 제거
    primeF = list(set(PollardRho(num)))

    result = num
    for i in primeF:
        result -= result // i

    return result


def main():
    N = int(input())
    print(EularPhi(N))


main()
