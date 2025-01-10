# 백준 10253

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


# 최대공약수
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


# 최소공배수
def lcm(a, b):
    return a * b // gcd(a, b)


# 분수 A를 분수 B로 뺐을 때 양수인지 체크
def check(A, B):
    common = lcm(A[1], B[1])

    temp = A[0] * (common // A[1]) - (common // B[1])
    if temp >= 0:
        return [True, temp, common]
    else:
        return [False, None, None]


def solve():
    num = [a, b]
    sub = [1, 1]

    # 이분 탐색으로 가장 큰 단위분수 빼기
    while True:
        start = 2
        end = 10**10

        while end - start > 1:
            mid = (end + start) // 2
            temp = check(num, [1, mid])
            if temp[0] == True:
                end = mid
            else:
                start = mid

        temp1 = check(num, [1, start])
        temp2 = check(num, [1, end])
        if temp1[0] == True:
            num = [temp1[1], temp1[2]]
            sub = [1, start]
        else:
            num = [temp2[1], temp2[2]]
            sub = [1, end]

        if num[0] == 0:
            return sub[1]


# main 함수 ----------
T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print(solve())