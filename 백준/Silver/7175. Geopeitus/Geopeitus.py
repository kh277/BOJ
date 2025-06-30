# 백준 7175

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(string, N, x):
    val = [i[0] for i in x]
    numX = dict()
    for i in range(N):
        numX[x[i][0]] = x[i][1].split(",")
    posX = dict()
    
    for i in range(len(string)):
        for j in range(N):
            if string[i] == x[j][0]:
                if x[j][0] in posX:
                    posX[x[j][0]].append(i)
                else:
                    posX[x[j][0]] = [i]

    result = []
    if N == 1:
        for i in range(len(numX[val[0]])):
            temp = string[:]
            temp = temp.replace(val[0], numX[val[0]][i])
            result.append(temp)
    elif N == 2:
        for i in range(len(numX[val[0]])):
            for j in range(len(numX[val[1]])):
                temp = string[:]
                temp = temp.replace(val[0], numX[val[0]][i])
                temp = temp.replace(val[1], numX[val[1]][j])
                result.append(temp)
    else:
        for i in range(len(numX[val[0]])):
            for j in range(len(numX[val[1]])):
                for k in range(len(numX[val[2]])):
                    temp = string[:]
                    temp = temp.replace(val[0], numX[val[0]][i])
                    temp = temp.replace(val[1], numX[val[1]][j])
                    temp = temp.replace(val[2], numX[val[2]][k])
                    result.append(temp)

    return result


def main():
    string = input().decode().rstrip()
    N = int(input())
    x = []
    for _ in range(N):
        x.append(list(input().decode().rstrip().split("=")))
    for i in solve(string, N, x):
        print(i)


main()
