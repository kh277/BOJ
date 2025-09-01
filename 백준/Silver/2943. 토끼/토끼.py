# 백준 2943

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, single, cup, sqrt, S, A):
    start = A
    end = S+A-1
    result = 0

    # 시작 부분을 성냥갑에 추가
    while (start % sqrt) != 0 and start <= end:
        single[start] += 1
        result += single[start]
        start += 1

    # 끝 부분이 N 미만인 경우 컵에 추가
    if end == N-1 and N % sqrt != 0 and N - (N%sqrt) >= start:
        cup[N//sqrt] += 1
        result += cup[N//sqrt]
        end = N - (N%sqrt) - 1

    # 끝 부분을 성냥갑에 추가
    while (end + 1) % sqrt != 0 and start <= end:
        single[end] += 1
        result += single[end]
        end -= 1

    # 중간 부분을 컵에 추가
    while start <= end:
        curCup = start//sqrt
        cup[curCup] += 1
        result += cup[curCup]
        start += sqrt

    return result


def main():
    N, M = map(int, input().split())
    sqrt = int(N**0.5)
    single = array('I', [0]) * N
    cup = array('I', [0]) * (N//sqrt+1)
    for _ in range(M):
        S, A = map(int, input().split())
        print(solve(N, single, cup, sqrt, S, A-1))


main()
