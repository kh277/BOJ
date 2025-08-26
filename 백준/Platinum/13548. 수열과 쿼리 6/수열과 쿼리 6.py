# 백준 13548

'''
count[i] = 현재 구간에 존재하는 숫자 i의 개수
freq[i] = 현재 구간의 count배열에서 값이 i인 수의 개수
'''

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
ARRAY_TYPE = 'i'
INF = 10**5


def solve(N, M, A, query):
    sqrt = N**0.5
    result = array(ARRAY_TYPE, [0]) * M
    count = array(ARRAY_TYPE, [0]) * INF
    freq = array(ARRAY_TYPE, [0]) * N
    query.sort(key= lambda x: (x[0]//(sqrt), x[1]))

    curRes = 0
    prevS = 0
    prevE = -1

    # 쿼리 처리
    for i in range(M):
        curS, curE, index = query[i]

        while curS < prevS:
            prevS -= 1
            freq[count[A[prevS]]] -= 1
            count[A[prevS]] += 1
            curRes = max(curRes, count[A[prevS]])
            freq[count[A[prevS]]] += 1

        while curS > prevS:
            freq[count[A[prevS]]] -= 1
            if freq[count[A[prevS]]] == 0 and curRes == count[A[prevS]]:
                curRes -= 1
            count[A[prevS]] -= 1
            freq[count[A[prevS]]] += 1
            prevS += 1

        while curE < prevE:
            freq[count[A[prevE]]] -= 1
            if freq[count[A[prevE]]] == 0 and curRes == count[A[prevE]]:
                curRes -= 1
            count[A[prevE]] -= 1
            freq[count[A[prevE]]] += 1
            prevE -= 1

        while curE > prevE:
            prevE += 1
            freq[count[A[prevE]]] -= 1
            count[A[prevE]] += 1
            curRes = max(curRes, count[A[prevE]])
            freq[count[A[prevE]]] += 1

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
