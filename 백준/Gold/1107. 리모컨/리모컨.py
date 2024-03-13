# 백준 1107

'''
이 문제는 사용할 수 있는 버튼들을 가지고 목표 채널 N과 가장 가까운 숫자를 구해야 한다.

생각1
가능한 케이스들은 다음과 같다.
1. 100에서 +, -만 사용해서 이동하는 경우.
2. 숫자를 직접 입력해서 바로 이동하는 경우.
3. 근처 채널로 이동한 뒤 +, -를 사용하여 이동하는 경우.

각 케이스의 값을 구한 뒤, 최소값을 출력하면 된다.
'''

import sys

input = sys.stdin.readline


def is_possible(N: int, length: int, digit: set) -> int:
    # 각 자리수가 digit에 존재하는지 확인
    for i in range(length):
        num = N % 10
        if num not in digit:
            return -1
        N = N // 10

    return length


def solve(N: int, digit: list) -> int:

    # 1. 100에서 +, -만 사용해서 이동하는 경우
    case_1 = abs(N-100)

    # 2. 숫자를 직접 입력해서 바로 이동하는 경우
    case_2 = is_possible(N, len(str(N)), set(digit))

    # 2번 케이스가 불가능한 경우
    if case_2 == -1:
        case_2 = 10000000

    # 3. 근처 채널로 이동한 뒤 +, -를 사용해서 이동하는 경우
    case_3 = 10000000

    # 이동 가능한 모든 채널에 대해
    for i in range(0, 1000001):
        temp = is_possible(i, len(str(i)), set(digit))
        if temp == -1:
            continue

        # 이동이 가능하다면
        else:
            count = temp + abs(N-i)
            if count < case_3:
                case_3 = count

    return min(case_1, case_2, case_3)


def main():
    N = int(input())
    M = int(input())
    digit = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

    # 사용 가능한 버튼만 인자로 넘겨줌
    if M != 0:
        button = list(map(int, input().split()))
        for i in button:
            digit.remove(i)

    print(solve(N, list(digit)))


main()
