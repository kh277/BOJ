# 백준 27172

'''
A % B = 0이면 B가 승리하게 된다.
예를 들어 B가 3이면, 3의 배수를 가진 모든 사람들에게 승리할 수 있다.

에라토스테네스의 체의 원리를 이용하여 결과를 계산한다.
'''

import sys

input = sys.stdin.readline


def solve(N: int, num: list) -> list:
    # 수가 겹치지 않으므로 속도가 빠른 set 사용
    set_num = set(num)
    max_data = max(set_num)
    score = [0 for i in range(max_data+1)]
    
    # 모든 플레이어가 가진 수에 대해서 반복
    for i in set_num:
        # 현재 탐색하고자 하는 플레이어가 가진 수의 배수 숫자에 연산 적용
        for j in range(i*2, max_data+1, i):
            if j in set_num:
                score[i] += 1
                score[j] -= 1
    
    # set(set_num)는 순서가 없으므로 set로 변경하기 이전 자료(num) 사용
    return [score[i] for i in num]


def main():
    N = int(input())
    num = list(map(int, input().split()))

    print(*solve(N, num))


main()