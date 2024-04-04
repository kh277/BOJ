# 백준 16953

'''
A에서 주어진 연산을 사용하여 B로 도달할 수 있다는 것은
B에서 역연산을 하면 A로 도달할 수 있다는 것을 의미한다.
따라서 B에서 짝수이면 2로 나누고, 마지막 자리 수가 1이면 1을 떼고, 그 외의 경우엔 -1을 출력한다.
'''

import sys

input = sys.stdin.readline


def solve(A: int, B: int) -> int:
    count = 0
    while True:
        count += 1

        # A와 B가 같아진 경우
        if B == A:
            return count
        
        # 수가 A보다 작아진 경우
        elif B < A:
            return -1

        # B가 짝수라면
        if B % 2 == 0:
            B = B // 2
        
        # B의 마지막 자리가 1이라면
        elif str(B)[-1] == '1':
            B = int(str(B)[:-1])

        else:
            return -1


def main():
    A, B = map(int, input().split())

    print(solve(A, B))


main()