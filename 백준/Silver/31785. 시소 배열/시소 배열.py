# 백준 31785

'''
중간에 값의 변경이 이루어지지 않으므로 누적 합으로 해결할 수 있다.
'''

import sys

input = sys.stdin.readline


def solve(A, prefixSum, query):
    temp = 0
    # 값 추가 쿼리
    if query[0] == 1:
        
        A.append(query[1])
        prefixSum.append(prefixSum[-1]+query[1])
        return A, prefixSum, []

    # 원소 삭제 쿼리
    else:
        mid = len(A)//2
        
        # 앞 부분이 더 클 경우
        if prefixSum[mid-1] > prefixSum[-1] - prefixSum[mid-1]:
            temp = prefixSum[-1] - prefixSum[mid-1]
            A = A[:mid]
            prefixSum = prefixSum[:mid]
        
        # 뒷 부분이 더 크거나 같을 경우
        else:
            temp = prefixSum[mid-1]
            A = A[mid:]
            prefixSum = prefixSum[mid:]
            for i in range(len(prefixSum)):
                prefixSum[i] -= temp

    return A, prefixSum, [temp]


# main 함수 ----------
Q = int(input())

A = []
prefixSum = []

# 첫 번째 쿼리 처리
query = list(map(int, input().split()))
A.append(query[1])
prefixSum.append(query[1])

# 첫 번째 쿼리 이후의 쿼리 처리
for i in range(1, Q):
    query = list(map(int, input().split()))
    A, prefixSum, temp = solve(A, prefixSum, query)
    if len(temp) != 0:
        print(*temp)

print(*A)
