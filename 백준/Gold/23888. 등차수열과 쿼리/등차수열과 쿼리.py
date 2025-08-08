# 백준 23888

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def GCD(a, b):
    while b > 0:
        a, b = b, a % b
    return a


# 등차수열의 [left, right]항까지의 합 출력
def query(a, d, left, right):
    result = right*(2*a + (right-1)*d)//2 - (left-1)*(2*a + (left-2)*d)//2
    return result


# 등차수열의 [left, right]항까지의 GCD 반환
def getGcd(a, d, left, right):
    if right - left >= 1:
        return GCD(GCD(a+(left-1)*d, a+(right-1)*d), a+left*d)
    else:
        return a+(left-1)*d


def main():
    a, d = map(int, input().split())
    q = int(input())
    for _ in range(q):
        t, l, r = map(int, input().split())
        if t == 1:
            print(query(a, d, l, r))
        else:
            print(getGcd(a, d, l, r))

main()
