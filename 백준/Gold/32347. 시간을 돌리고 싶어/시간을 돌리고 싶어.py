# 백준 32347

'''
매개변수 탐색으로 T의 최소값 찾기
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


# T일 이내 이동을 K번 이하로 하여 1일에 도달할 수 있는지 체크 
def check(T, K, gap):
    acc = 0
    for i in range(len(gap)):
        if acc + gap[i] <= T:
            acc += gap[i]
        else:
            if gap[i] > T:
                return False
            acc = gap[i]
            K -= 1

    if K >= 1:
        return True
    return False


def solve(N, K, A):
    A[N-1] = 1

    # 타임머신을 켜둔 간격 계산
    gap = []
    prev = 0
    for i in range(1, N):
        if A[i] == 1:
            gap.append(i-prev)
            prev = i

    # 이분 탐색으로 T의 최소값 찾기
    start = 0
    end = N-1
    while start < end:
        mid = (start+end)//2
        if check(mid, K, gap) == False:
            start = mid+1
        else:
            end = mid

    return start


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    print(solve(N, K, A[::-1]))


main()
