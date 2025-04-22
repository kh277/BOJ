# 백준 5615

'''
S = 2xy+x+y이고, 2S+1 = (2x+1)(2y+1)이다.
따라서 2S+1이 소수이면 있을 수 없는 면적이 된다.
'''

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
    testInt = [2, 3, 5, 7, 11]
    for i in testInt:
        if num == i:
            return True
        if num > 11 and MillerRabin(num, i) == True:
            return False
    if num <= 11:
        return False

    return True


def main():
    N = int(input())
    count = 0
    for _ in range(N):
        S = int(input())
        if S < 4 or isPrime(S*2+1) == True:
            count += 1
    
    print(count)


main()
