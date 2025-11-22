# 백준 14584

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def change(string):
    result = []
    for i in range(len(string)):
        result.append(chr((ord(string[i])-97+1)%26 + 97))

    return ''.join(result)


def solve(enc, words):
    for _ in range(26):
        flag = False
        for w in words:
            if w in enc:
                flag = True

        if flag == True:
            return enc

        enc = change(enc)


def main():
    enc = input().decode().rstrip()
    N = int(input())
    words = []
    for _ in range(N):
        words.append(input().decode().rstrip())
    print(solve(enc, words))


main()
