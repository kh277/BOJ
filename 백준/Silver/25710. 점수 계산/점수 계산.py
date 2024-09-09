# 백준 25710

'''
배열 a는 길이가 N이며, i번째 원소는 a_i가 된다.
두 원소의 곱을 구하고, 자릿수를 더한 총합을 구해야 하는데,
N <= 10만이므로 O(N^2)으로는 통과하지 못한다.
그러나 배열 a의 모든 원소는 1~999 사이의 정수이다.
따라서 비둘기집 원리에 의해 10만개의 배열 내에 반드시 중복이 발생하게 된다.
a_i * a_j을 구해야 하는데, 같은 수로만 이루어진 배열이 있을 수 있으므로
같은 수는 2개까지 허용하여 저장하도록 한다.
중복을 제거하고 나면 N은 최대 1998개이므로 O(N^2) 내에 통과가 가능하게 된다.

주의 반례
2
1 1
-> 1
'''

import sys

input = sys.stdin.readline


def num_sum(num: str) -> int:
    result = 0
    for i in num:
        result += int(i)
    
    return result


def solve(N: int, a: list) -> int:
    num = set()     # 중복되지 않은 원소 저장
    num_2 = set()   # 한 번만 중복된 원소 저장
    for i in range(N):
        if a[i] in num and a[i] not in num_2:
            num_2.add(a[i])
        elif a[i] not in num:
            num.add(a[i])
    
    # a_i * a_j의 자릿수 계산
    result = 0
    a = list(num) + list(num_2)
    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
            result = max(result, num_sum(str(a[i]*a[j])))
    
    return result
            

def main():
    N = int(input())
    a = list(map(int, input().split()))
    
    print(solve(N, a))


main()