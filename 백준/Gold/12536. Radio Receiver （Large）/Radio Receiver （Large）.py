# 백준 12535

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
epsilon = 10**(-12)


def check(N, mes, D):
    curS = mes[0][0] - D
    curE = mes[0][0] + D
    curT = mes[0][1]

    for i in range(1, N):
        gap = mes[i][1] - curT
        nextS = max(curS-gap, mes[i][0]-D)
        nextE = min(curE+gap, mes[i][0]+D)

        if nextS > nextE:
            return False

        curS = nextS
        curE = nextE
        curT = mes[i][1]

    return True


def solve(N, mes):
    mes.sort(key= lambda x: (x[1]))
    start = 0
    end = 10**10
    repeat = 0
    while repeat < 100:
        mid = (start+end)/2
        if check(N, mes, mid) == True:
            end = mid
        else:
            start = mid

        repeat += 1

    return end


def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        mes = []
        for _ in range(N):
            mes.append(list(map(int, input().split())))
        print(f"Case #{i+1}: {solve(N, mes)}")


main()
