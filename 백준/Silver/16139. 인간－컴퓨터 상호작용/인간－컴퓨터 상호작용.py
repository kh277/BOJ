# 백준 16139

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
asciiA = ord('a')


def init(L, S):
    data = [[0 for _ in range(L)] for _ in range(26)]
    data[ord(S[0])-asciiA][0] = 1

    for i in range(1, L):
        for c in range(26):
            data[c][i] = data[c][i-1]
        data[ord(S[i])-asciiA][i] += 1
    
    return data


def query(data, a, l, r):
    if l == 0:
        return data[ord(a)-asciiA][r]

    return data[ord(a)-asciiA][r] - data[ord(a)-asciiA][l-1]


def main():
    S = input().decode().rstrip()
    L = len(S)
    data = init(L, S)
    q = int(input())
    for _ in range(q):
        a, l, r = map(str, input().decode().rstrip().split())
        print(query(data, a, int(l), int(r)))


main()
