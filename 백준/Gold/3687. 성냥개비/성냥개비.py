# 백준 3687

'''
큰 수 만들기 -> 1, 7만 사용

작은 수 만들기 -> 7k+a 형태 구하기
7k+7 -> 8 + 888...
7k+8 -> 10 + 888...
7k+9 -> 18 + 888...
7k+(10+7) -> 200 + 888...
7k+11 -> 20 + 888...
7k+12 -> 28 + 888...
7k+13 -> 68 + 888...
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N):
    if N == 2:
        return [1, 1]
    elif N == 3:
        return [7, 7]

    # 큰 수 만들기
    bigResult = 0
    if N % 2 == 0:
        bigResult = int('1' * (N//2))
    else:
        bigResult = int('7' + '1' * ((N-3)//2))
    
    # 작은 수 만들기
    smallResult = 0
    oneDigit = [0, 0, 1, 7, 4, 2, 6, 8]
    if 2 <= N <= 7:
        smallResult = oneDigit[N]
    else:
        if (N-7) % 7 == 0:
            smallResult = int('8' * (N//7))
        elif (N-7) % 7 == 1:
            smallResult = int('10' + '8' * ((N-8)//7))
        elif (N-7) % 7 == 2:
            smallResult = int('18' + '8' * ((N-9)//7))
        elif (N-7) % 7 == 3:
            if N == 10:
                smallResult = 22
            else:
                smallResult = int('200' + '8' * ((N-17)//7))
        elif (N-7) % 7 == 4:
            smallResult = int('20' + '8' * ((N-11)//7))
        elif (N-7) % 7 == 5:
            smallResult = int('28' + '8' * ((N-12)//7))
        elif (N-7) % 7 == 6:
            smallResult = int('68' + '8' * ((N-13)//7))

    return [smallResult, bigResult]


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(*solve(N))


main()
