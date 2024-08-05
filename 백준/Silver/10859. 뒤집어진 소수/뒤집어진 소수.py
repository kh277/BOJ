# 백준 11558

import sys

input = sys.stdin.readline


def is_prime(N: int) -> bool:
    if N <= 1:
        return False
    
    # 2, 3의 경우 소수로 판단
    if N <= 3:
        return True

    # 2, 3으로 나누어 떨어지면 소수가 아니라고 판단
    if N % 2 == 0 or N % 3 == 0:
        return False

    # 6k ± 1 형태의 수를 사용하여 소수 판별
    for i in range(5, int(N**0.5)+1, 6):
        if N % i == 0 or N % (i + 2) == 0:
            return False

    return True


def solve(N: int) -> str:
    result = ''

    for i in reversed(str(N)):
        if int(i) in [0, 1, 2, 5, 8]:
            result += i
        elif int(i) == 6:
            result += '9'
        elif int(i) == 9:
            result += '6'
        else:
            return 'no'
    
    return 'yes' if is_prime(int(result)) and is_prime(N) else 'no' 


def main():
    N = int(input())

    print(solve(N))


main()