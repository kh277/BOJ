# 백준 32627

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, M, S):
    data = []
    for i in range(N):
        data.append([S[i], i])

    # 정렬 후 문자 M개 제거
    data.sort(key= lambda x: (x[0], x[1]))
    data = data[M:]

    # 인덱스 순서로 재정렬
    data.sort(key= lambda x: (x[1], x[0]))
    return ''.join([i[0] for i in data])


def main():
    N, M = map(int, input().split())
    S = input().decode().rstrip()
    print(solve(N, M, S))


main()
