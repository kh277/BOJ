# 백준 3178

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def countNode(N, K, word):
    result = K
    word.sort()
    for i in range(1, N):
        connect = True
        for j in range(K):
            if connect == False:
                result += K-j
                break
            elif word[i-1][j] != word[i][j]:
                result += 1
                connect = False

    return result


def solve(N, K, word1, word2):
    result = countNode(N, K, word1)
    result += countNode(N, K, word2)

    return result


def main():
    N, K = map(int, input().split())
    word1 = []
    word2 = []
    for _ in range(N):
        w = input().decode().strip()
        word1.append(w[:K])
        word2.append(w[K:][::-1])


    print(solve(N, K, word1, word2))


main()
