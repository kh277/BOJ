# 백준 2108

from sys import stdin

input = stdin.readline


def solve(N: int, L: list) -> list:
    L.sort()

    # 평균값 추출
    sum = 0
    for i in L:
        sum += i

    # 딕셔너리를 만들어 최빈값 추출
    dic = dict()
    for i in L:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    dic = sorted(dic.items(), key= lambda x: x[1], reverse=True)
    mode = dic[0][0]

    # 최빈값이 2개 이상 존재한다면
    if len(dic) > 1 and dic[0][1] == dic[1][1]:
        mode = dic[1][0]

    return [round(sum/N), L[N//2], mode, L[N-1] - L[0]]


def main():
    N = int(input())
    L = [0 for _ in range(N)]

    for i in range(N):
        L[i] = int(input())

    for i in solve(N, L):
        print(i)


main()
