# 백준 26975

'''
소가 N마리 있고, 각 소가 지불할 의향이 있는 최대 등록금 C가 주어질 때,
학비를 얼마로 설정해야 이익이 최대가 되는지를 구하는 문제이다.

C에 들어있는 원소를 증가하는 순서대로 탐색한다.
등록금을 c_1로 설정할 경우, 이익은 c_1*len(c_1 이상인 값의 개수)가 된다.
위 과정을 반복하면 된다.
'''

import sys

input = sys.stdin.readline


def solve():
    C.sort()
    index = 0               # C에서 등록금을 가리킬 인덱스
    result = [0, 0]     # [총 얻을 수 있는 등록금, 등록금]
    beforeTuition = 0       # 이전 인덱스에서의 등록금 값

    while index < N:
        if beforeTuition == C[index]:
            index += 1
            continue
        
        sumTuition = (N-index)*C[index]
        if sumTuition > result[0]:
            result = [sumTuition, C[index]]
        
        beforeTuition = C[index]
        index += 1

    return result


# main 함수 ----------
N = int(input())
C = list(map(int, input().split()))
print(*solve())