# 백준 30970

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(data):
    result = [[], []]

    # 품질 정렬
    data.sort(key= lambda x: (-x[0], x[1]))
    result[0].append(data[0][0])
    result[0].append(data[0][1])
    result[0].append(data[1][0])
    result[0].append(data[1][1])

    # 가격 정렬
    data.sort(key= lambda x: (x[1], -x[0]))
    result[1].append(data[0][0])
    result[1].append(data[0][1])
    result[1].append(data[1][0])
    result[1].append(data[1][1])

    return result


def main():
    N = int(input())
    data = []
    for _ in range(N):
        data.append(list(map(int, input().split())))

    for i in solve(data):
        print(*i)


main()
