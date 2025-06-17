# 백준 31908

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, data):
    result = []
    for i in data.keys():
        if i != '-' and len(data[i]) == 2:
            result.append(data[i])
            
    return result


def main():
    N = int(input())
    data = dict()
    for _ in range(N):
        name, ring = input().decode().split()
        if ring in data:
            data[ring].append(name)
        else:
            data[ring] = [name]

    result = solve(N, data)
    print(len(result))
    for i in result:
        print(*i)


main()
