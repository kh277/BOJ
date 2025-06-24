# 백준 9734

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def GCD(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def solve(intPart, nonRPart, repeatPart):
    if repeatPart[-1] == ')':
        repeatPart = repeatPart[:-1]

    lower = int('9'*len(repeatPart)) * 10**(len(nonRPart))
    upper = lower*int(intPart)
    if len(nonRPart) == 0:
        upper += int(repeatPart)
    else:
        upper = lower*int(intPart) + int(nonRPart)*10**(len(repeatPart)) + int(repeatPart) - int(nonRPart)

    gcd = GCD(upper, lower)
    return [upper//gcd, lower//gcd]


def main():
    while True:
        try:
            intPart, floatPart = map(str, input().decode().strip().split('.'))
            nonRPart, repeatPart = map(str, floatPart.split('('))
            result = solve(intPart, nonRPart, repeatPart)
            print(f"{intPart}.{floatPart} = {result[0]} / {result[1]}")
        except:
            break


main()
