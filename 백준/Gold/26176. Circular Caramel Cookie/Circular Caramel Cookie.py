# 백준 26176

import io
import math

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


# 반지름이 R인 와플이 포함할 수 있는 완전한 정사각형 개수 반환
def check(R):
    count = 0
    prevY = int(R)
    R2 = int(R*R)
    for x in range(1, int(R)+1):
        curY = math.isqrt(R2 - x*x)
        count += min(prevY, curY)
        prevY = curY

    return count*4


def solve(N):
    no = 0
    yes = 32000
    repeat = 0
    while repeat < 40:
        mid = (yes+no)/2
        if check(mid) > N:
            yes = mid
        else:
            no = mid
        repeat += 1

    return yes


def main():
    N = int(input())
    print(solve(N))


main()
