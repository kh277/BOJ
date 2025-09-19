# 백준 34457

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, data):
    # S가 존재하는 구간 저장
    gap = []
    start = -1
    for i in range(N):
        if start == -1 and data[i] == 1:
            start = i
        elif start != -1 and data[i] == 0:
            gap.append([start, i-1])
            start = -1
    if start != -1:
        gap.append([start, N-1])

    # 반례 처리
    if len(gap) == 1 and gap[0][0] == 0 and gap[0][1] == N-1:
        return N-1

    # 두 구간의 차이가 1일 때 합치기
    result = 1
    if len(gap) > 0:
        result = max([min(e-s+2, N) for s, e in gap])
    for i in range(1, len(gap)):
        if gap[i][0] - gap[i-1][1] == 2:
            result = max(result, gap[i][1]-gap[i-1][0]+1)

    return result


def main():
    N = int(input())
    data = array('b')
    for _ in range(N):
        data.append(1 if input().decode().rstrip() == 'S' else 0)
    print(solve(N, data))


main()
