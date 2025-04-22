# 백준 25821

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


def millerRabin(num, base):
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
    test = [2, 325, 9375, 28178, 450775, 9780504, 1795265022]
    for i in test:
        if num == i:
            return True
        if num > 40 and millerRabin(num, i) == True:
            return False
    if num <= 40:
        return False

    return True


# A, B 구간에서 팰린드롬 수 체크
def solve(A, B):
    primeCount = 0

    # 1자리, 2자리 팰린드롬 소수 체크
    for i in [2, 3, 5, 7, 11]:
        if A <= i <= B:
            primeCount += 1

    # 3자리 이상의 소수 체크
    for curL in range(max(3, len(str(A))), len(str(B))+1):
        start = 10**((curL+1)//2 - 1)
        end = 10**((curL+1)//2)

        # 범위 내의 홀수에 대해 체크
        for n in range(start, end):
            strI = str(n)
            if int(strI[0]) % 2 == 0:
                continue

            if curL % 2 == 0:
                temp = int(strI + strI[::-1])
            else:
                temp = int(strI + strI[:-1][::-1])

            if temp > B:
                break
            if temp < A:
                continue

            # 소수 판별
            if isPrime(temp) == True:
                primeCount += 1

    return primeCount


def main():
    A, B = map(int, input().split())
    print(solve(A, B))


main()