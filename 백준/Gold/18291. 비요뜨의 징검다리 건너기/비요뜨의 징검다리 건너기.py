# 백준 18291

'''
강을 건너는 방법은 몇 개의 징검다리를 건너는지의 합으로 볼 수 있다.
N=6일 경우 1번과 6번 징검다리는 반드시 지나야 하므로,
6개의 징검다리를 지나는 경우의 수 -> 4C4
5개의 징검다리를 지나는 경우의 수 -> 4C3
...
2개의 징검다리를 지나는 경우의 수 -> 4C0
로 볼 수 있다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve():
    if N == 1:
        return 1

    return pow(2, N-2, 1000000007)


# main 함수 ----------
T = int(input())
for _ in range(T):
    N = int(input())
    print(solve())