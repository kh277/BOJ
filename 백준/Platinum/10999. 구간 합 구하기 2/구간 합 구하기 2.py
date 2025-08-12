# 백준 10999

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


# addQuery에서 구간 [left, right]에 변경된 값의 총합 반환
def query(left, right, addQuery):
    result = 0
    for start, end, value in addQuery:
        if right >= start and end >= left:
            result += (min(right, end)-max(left, start)+1)*value

    return result


def main():
    N, M, K = map(int, input().split())

    A = []
    for _ in range(N):
        A.append(int(input()))

    # A 누적합 계산
    accSum = [0 for _ in range(N)]
    accSum[0] = A[0]
    for i in range(1, N):
        accSum[i] = accSum[i-1] + A[i]

    # 쿼리 처리
    addQuery = []
    for _ in range(M+K):
        q = list(map(int, input().split()))
        # 1: 더하기 쿼리 저장
        if q[0] == 1:
            addQuery.append([q[1]-1, q[2]-1, q[3]])
        
        # 2: 수열 누적 합 + 더하기 쿼리에서 범위에 포함되는 값 합산
        else:
            gap = accSum[q[2]-1]
            if q[1]-1 > 0:
                gap -= accSum[q[1]-2]
            print(gap + query(q[1]-1, q[2]-1, addQuery))


main()
