# 백준 32136

'''
난방기의 위치를 x로 두면, 모든 얼음을 녹이는 시간 f(x)는 아래로 볼록인 그래프를 가지게 된다.
구하고자 하는 min(f(x))은 삼분 탐색으로 NlogN에 구할 수 있다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**15


# 히터가 x위치에 있을 때 Tx
def check(N, A, x):
    result = 0
    for i in range(0, x):
        result = max(result, (x-i)*A[i])
    for i in range(x+1, N):
        result = max(result, (i-x)*A[i])

    return result


def solve(N, A):
    start = 0
    end = N-1

    # 삼분 탐색으로 가동 시간을 최소로 만드는 지점 찾기
    while end - start > 2:
        mid1 = (start*2+end)//3
        mid2 = (start+end*2)//3

        if check(N, A, mid1) > check(N, A, mid2):
            start = mid1+1
        else:
            end = mid2

    # 그 지점에서 최소 Ti값 찾기 
    result = INF
    for i in range(start, end+1):
        result = min(result, check(N, A, i))

    return result


def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(solve(N, A))


main()
