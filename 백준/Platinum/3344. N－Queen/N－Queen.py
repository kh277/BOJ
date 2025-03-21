# 백준 3344

'''
해당 링크에서 로직을 참고하여 구현했다.
링크 : https://en.wikipedia.org/wiki/Eight_queens_puzzle
'''

import io, os
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def arrayAppend(out, start, stop, step):
    for i in range(start, stop, step):
        out.append(i)


def solve(N):
    out = array('I')
    
    if N % 6 == 2:
        arrayAppend(out, 2, N+1, 2)
        out.append(3)
        out.append(1)
        arrayAppend(out, 7, N+1, 2)
        out.append(5)
    elif N % 6 == 3:
        arrayAppend(out, 4, N+1, 2)
        out.append(2)
        arrayAppend(out, 5, N+1, 2)
        out.append(1)
        out.append(3)
    else:
        arrayAppend(out, 2, N+1, 2)
        arrayAppend(out, 1, N+1, 2)

    return out


def main():
    N = int(input())
    os.write(1, "\n".join(map(str, solve(N))).encode("ascii"))


main()