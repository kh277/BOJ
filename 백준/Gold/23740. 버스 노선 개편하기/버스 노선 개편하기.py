# 백준 23740

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, data):
    data.sort(key= lambda x: (x[0], x[1]))

    result = []
    prevS, prevE, prevC = data[0]
    for i in range(1, N):
        curS, curE, curC = data[i]
        if prevE >= curS:
            prevE = max(prevE, curE)
            prevC = min(prevC, curC)
        else:
            result.append([prevS, prevE, prevC])
            prevS, prevE, prevC = data[i]
    result.append([prevS, prevE, prevC])

    return result


def main():
    N = int(input())
    data = []
    for _ in range(N):
        data.append(list(map(int, input().split())))

    result = solve(N, data)
    print(len(result))
    for i in result:
        print(*i)


main()
