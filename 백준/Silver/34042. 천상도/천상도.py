# 백준 34042

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, A):
    if N == 1:
        return A[0]

    data = array('I', [0]) * 5
    for i in A:
        data[i+2] += 1

    # 양수가 있는 경우
    if data[3] + data[4] >= 1:
        # 음수가 2개 이상 있는 경우
        if data[0] + data[1] >= 2:
            # 음수에 -2만 있는 경우
            if data[1] == 0:
                return 2**(data[0]//2*2+data[4])
            else:
                return 2**(data[0]+data[4])
        # 음수가 1개 이하이고 2가 있는 경우
        elif data[4] > 0:
            return 2**(data[4])
        # 음수가 1개 이하이고 2도 없는 경우
        else:
            return 1
    # 양수가 없는 경우
    else:
        # 음수가 2개 이상 있는 경우
        if data[0] + data[1] >= 2:
            # 음수에 -2만 있는 경우
            if data[1] == 0:
                return 2**(data[0]//2*2+data[4])
            else:
                return 2**(data[0]+data[4])
        # 음수가 1개 이하로 있는 경우
        else:
            if data[2] > 0:
                return 0
            elif data[3] > 0:
                return -1
            else:
                return -2


def main():
    N, M = map(int, input().split())
    for _ in range(M):
        A = list(map(int, input().split()))
        print(solve(N, A))


main()
