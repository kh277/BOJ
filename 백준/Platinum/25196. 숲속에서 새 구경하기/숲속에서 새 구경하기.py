# 백준 25196

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def GCD(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def LCM(a, b):
    return a * b // GCD(a, b)


# 주기가 bV이고 구간 [bS, bE]에 보이는 새가 구간 [start, end]에 보이는지 체크
def check(start, end, bird):
    bV, bS, bE = bird
    cycle = max(0, start//bV-1)

    result = []
    while True:
        curStart = bV*cycle + bS
        curEnd = bV*cycle + bE

        # 범위를 벗어난 경우
        if curStart > end:
            break

        # 공통 범위 저장
        if max(start, curStart) <= min(end, curEnd):
            result.append([max(start, curStart), min(end, curEnd)])

        cycle += 1

    return result


def solve(A, B, C):
    # 주기가 가장 큰 새를 A로 지정
    A, B, C = sorted((A, B, C), key= lambda x: -x[0])
    total = LCM(LCM(A[0], B[0]), C[0])

    for i in range(total//A[0]):
        # A와 B의 공통 범위 체크
        ab = check(i*A[0]+A[1], i*A[0]+A[2], B)

        if len(ab) > 0:
            for curS, curE in ab:
                # AB와 C의 공통 범위 체크
                abc = check(curS, curE, C)

                if len(abc) > 0:
                    return abc[0][0]

    return -1


def main():
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    print(solve(A, B, C))


main()