# 백준 10816

import sys

input = sys.stdin.readline


def solve(N: int, num: list, M: int, target: list) -> list:
    dic = dict()

    for i in range(N):
        if num[i] not in dic:
            dic[num[i]] = 1
        else:
            dic[num[i]] += 1
    
    result = []

    for i in range(M):
        temp = dic.get(target[i])
        if temp == None:
            result.append(0)
        else:
            result.append(temp)
    
    return result


def main():
    N = int(input())
    num = list(map(int, input().split()))
    M = int(input())
    target = list(map(int, input().split()))

    print(*solve(N, num, M, target))


main()