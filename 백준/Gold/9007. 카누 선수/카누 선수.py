# 백준 9007

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


# arr에서 target 이하인 값 중 최대의 값 탐색
def binarySearch(arr, target):
    yes = 0
    no = len(arr)-1

    while abs(yes-no) > 1:
        mid = (yes+no)//2
        if arr[mid] < target:
            yes = mid
        else:
            no = mid

    return yes


def solve(N, K, data):
    # 반을 2개씩 묶기
    A = set()
    B = set()
    for i in range(N):
        for j in range(N):
            A.add(data[0][i]+data[1][j])
            B.add(data[2][i]+data[3][j])

    # 정렬
    A = sorted(list(A))
    B = sorted(list(B))

    # K에 가까워지도록 하는 A+B 값 찾기
    gap = 10**9
    result = 0
    for iA in range(len(A)):
        # B에서 K에 가까워지는 최적의 값 찾기
        iB = binarySearch(B, K - A[iA])
        curGap = abs(K-A[iA]-B[iB])

        # iB 근처 값도 조사
        for i in range(iB, min(len(B), iB+3)):
            temp = abs(K-A[iA]-B[i])
            if curGap > temp:
                curGap = temp
                iB = i

        # 값 갱신
        if gap > curGap:
            gap = curGap
            result = A[iA]+B[iB]
        elif gap == curGap:
            result = min(result, A[iA]+B[iB])

    return result


def main():
    T = int(input())
    for _ in range(T):
        K, N = map(int, input().split())
        data = []
        for _ in range(4):
            data.append(list(map(int, input().split())))

        print(solve(N, K, data))


main()
