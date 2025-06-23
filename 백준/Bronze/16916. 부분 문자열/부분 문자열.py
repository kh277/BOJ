# 백준 16916

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def getFail(pattern):
    fail = [0 for _ in range(len(pattern))]

    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = fail[j-1]

        if pattern[i] == pattern[j]:
            j += 1
            fail[i] = j

    return fail


def KMP(text, pattern):
    fail = getFail(pattern)

    result = []
    j = 0
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = fail[j-1]

        if text[i] == pattern[j]:
            if j == len(pattern)-1:
                result.append(i-len(pattern)+2)
                j = fail[j]
            else:
                j += 1
    
    return result


def solve(S, P):
    if len(KMP(S, P)) > 0:
        return 1
    return 0


def main():
    S = input().decode().rstrip()
    P = input().decode().rstrip()
    print(solve(S, P))


main()
