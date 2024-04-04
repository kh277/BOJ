# 백준 12904

'''
S에서 주어진 연산을 사용하여 T로 도달할 수 있다는 것은
T에서 역연산을 하면 S로 도달할 수 있다는 것을 의미한다.
따라서 T의 마지막 문자가 A라면 A를 빼고, B라면 B를 빼고 문자열을 뒤집으면 된다.
'''

import sys

input = sys.stdin.readline


def solve(S: str, T: str) -> int:
    while True:
        # S와 T가 같아진 경우
        if len(S) == len(T):
            for i in range(len(T)):
                if T[i] != S[i]:
                    return 0
            return 1

        # T의 마지막 자리가 A인 경우
        if T[-1] == 'A':
            T = T[:-1]
        
        # T의 마지막 자리가 B인 경우
        elif T[-1] == 'B':
            T = T[:-1][::-1]


def main():
    S = input().rstrip()
    T = input().rstrip()

    print(solve(S, T))


main()