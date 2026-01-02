# 백준 27654

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


# N개의 시험 중 K개를 뽑아 평균값 ev를 만들 수 있는지 체크
def check(N, K, data, ev):
    data.sort(key= lambda x: (ev*x[1]-x[0]))
    accP = 0
    accQ = 0
    for i in range(K):
        accP += data[i][0]
        accQ += data[i][1]

    if accP/accQ >= ev:
        return True
    return False


def solve(N, K, data):
    yes = 0
    no = 1
    repeatCount = 0
    while repeatCount < 50:
        mid = (yes+no)/2
        if check(N, K, data, mid) == True:
            yes = mid
        else:
            no = mid
        repeatCount += 1

    return yes


def main():
    N, K = map(int, input().split())
    data = []
    for _ in range(N):
        data.append(tuple(map(int, input().split())))
    print(solve(N, K, data))


main()
