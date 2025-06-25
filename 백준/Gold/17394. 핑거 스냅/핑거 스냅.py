# 백준 17394

import io
from array import array
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 1000004


def LinearSieve(N):
    sieve = array('I', [0]) * (N+1)
    prime = array('I')

    for i in range(2, N+1):
        # 소수 추가
        if sieve[i] == 0:
            prime.append(i)
            sieve[i] = i

        # 합성수 제거
        for j in range(len(prime)):
            if i * prime[j] > N:
                break
            sieve[i * prime[j]] = prime[j]
            if i % prime[j] == 0:
                break

    return prime


def LowerBound(arr, target):
    start = 0
    end = len(arr)

    while start < end:
        mid = (start+end)//2
        if arr[mid] < target:
            start = mid+1
        else:
            end = mid

    return start


def BFS(start, end):
    q = deque()
    q.append(start)
    visited = array('i', [-1]) * INF
    visited[start] = 0

    if start in end:
        return 0

    while q:
        curN = q.popleft()
        for nextN in [curN//2, curN//3, curN+1, curN-1]:
            if 0 < nextN < INF and visited[nextN] == -1:
                q.append(nextN)
                visited[nextN] = visited[curN]+1
                if nextN in end:
                    return visited[curN]+1

    return -1


def solve(N, A, B, prime):
    # 구간 [A, B] 내의 소수 반환
    startIndex = LowerBound(prime, A)
    endIndex = LowerBound(prime, B)

    # 구간 내 소수가 없을 경우
    if endIndex < startIndex:
        return -1
    
    primeRange = prime[startIndex:endIndex+1]
    if primeRange[-1] > B:
        primeRange.pop()
    
    return BFS(N, set(primeRange))


def main():
    T = int(input())
    prime = LinearSieve(100003)
    for _ in range(T):
        N, A, B = map(int, input().split())
        print(solve(N, A, B, prime))


main()
