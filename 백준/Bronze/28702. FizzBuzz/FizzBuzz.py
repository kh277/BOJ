# 백준 28702

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(A, B, C):
    s = {'Fizz', 'Buzz', 'FizzBuzz'}
    target = 0
    if A not in s:
        target = int(A)+3
    elif B not in s:
        target = int(B)+2
    else:
        target = int(C)+1

    if target % 3 == 0 and target % 5 == 0:
        return 'FizzBuzz'
    elif target % 3 == 0:
        return 'Fizz'
    elif target % 5 == 0:
        return 'Buzz'
    else:
        return target


def main():
    A = input().decode().rstrip()
    B = input().decode().rstrip()
    C = input().decode().rstrip()

    print(solve(A, B, C))


main()
