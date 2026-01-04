# 백준 26040

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(A, B):
    result = []
    for i in A:
        if i in B:
            result.append(chr(ord(i)+32))
        else:
            result.append(i)
    
    return ''.join(result)


def main():
    A = input().decode().rstrip()
    B = set(input().decode().rstrip())
    print(solve(A, B))


main()
