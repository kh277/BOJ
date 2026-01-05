# 백준 9007

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, K, a, b, c, d):
    # 반을 2개씩 묶기
    A = []
    B = []
    for i in range(N):
        for j in range(N):
            A.append(a[i]+b[j])
            B.append(c[i]+d[j])

    # 정렬
    A.sort()
    B.sort()

    # K에 가까워지도록 하는 A+B 값 찾기
    iA = 0
    iB = len(B)-1
    bestSum = 10**9
    bestGap = 10**9
    while iA < len(A) and iB >= 0:
        curSum = A[iA] + B[iB]
        diff = K - curSum
        curGap = abs(diff)

        if curGap < bestGap or (curGap == bestGap and curSum < bestSum):
            bestSum = curSum
            bestGap = curGap
            if bestGap == 0:
                return bestSum

        if diff > 0:
            iA += 1
        else:
            iB -= 1
    
    return bestSum


def main():
    T = int(input())
    for _ in range(T):
        K, N = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        c = list(map(int, input().split()))
        d = list(map(int, input().split()))

        print(solve(N, K, a, b, c, d))


main()
