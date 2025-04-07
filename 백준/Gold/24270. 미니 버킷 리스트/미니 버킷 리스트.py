# 백준 24270

'''
모든 일을 길이가 1인 시간으로 바꾸고 줄인 시간만큼 전체 길이에서 빼준다.
그 뒤 (전체 길이)P(일의 개수)를 계산하면 된다.

ex)
4 1000
3 4 5 6 의 예시에서 일을 전부 길이가 1인 시간으로 바꿀 수 있다.
이 경우 전체 시간 986에 1, 1, 1, 1인 일을 배치하는 문제로 바뀐다.
따라서 986P4이 된다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
MOD = 1000000007


def solve(N, K, work):
    sub = 0
    for i in work:
        sub += i-1

    total = K - sub
    result = 1
    for _ in range(N):
        result = (result * total) % MOD
        total -= 1
    
    return result


def main():
    N, K = map(int, input().split())
    work = list(map(int, input().split()))

    print(solve(N, K, work))


main()