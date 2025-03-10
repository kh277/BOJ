# 백준 29790

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, U, L):
    maple = False
    boj = False

    if N >= 1000:
        boj = True
    if U >= 8000 or L >= 260:
        maple = True

    if boj == True and maple == True:
        return 'Very Good'
    elif boj == True:
        return 'Good'
    else:
        return 'Bad'


def main():
    N, U, L = map(int, input().split())
    print(solve(N, U, L))


main()