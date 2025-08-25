# 백준 13547

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
ARRAY_TYPE = 'i'
INF = 10**6


def solve(N, M, A, query):
    sqrt = N**0.5
    result = array(ARRAY_TYPE, [0]) * M
    freq = array(ARRAY_TYPE, [0]) * INF
    query.sort(key= lambda x: (x[0]//sqrt, x[1]))

    curRes = 0
    prevS = 0
    prevE = -1

    # 쿼리 처리
    for i in range(M):
        curS, curE, index = query[i]

        while curS < prevS:
            prevS -= 1
            if freq[A[prevS]] == 0:
                curRes += 1
            freq[A[prevS]] += 1

        while curS > prevS:
            freq[A[prevS]] -= 1
            if freq[A[prevS]] == 0:
                curRes -= 1
            prevS += 1

        while curE < prevE:
            freq[A[prevE]] -= 1
            if freq[A[prevE]] == 0:
                curRes -= 1
            prevE -= 1

        while curE > prevE:
            prevE += 1
            if freq[A[prevE]] == 0:
                curRes += 1
            freq[A[prevE]] += 1

        prevS = curS
        prevE = curE
        result[index] = curRes

    return result


def main():
    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    query = []
    for i in range(M):
        s, e = map(int, input().split())
        query.append([s-1, e-1, i])

    for i in solve(N, M, A, query):
        print(i)


main()
