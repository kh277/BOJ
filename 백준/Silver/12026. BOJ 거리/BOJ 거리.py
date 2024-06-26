# 백준 12026

'''
DP[i] = 1에서 i번째 보도블럭까지 이동하는데 필요한 에너지 양의 최소값
'''

import sys

input = sys.stdin.readline
INF = 10e8


def solve(N: int, string: str) -> int:
    DP = [INF for _ in range(N)]
    text = ['B', 'O', 'J']

    DP[0] = 0

    # Bottom-Up 방식
    for cur in range(0, N):
        # 첫 글자가 B, O, J에 해당하는 경우 따라 구별
        for case in range(3):
            cur_text = text[case]
            next_text = text[(case+1)%3]
            if string[cur] == cur_text:
                # 현재 이후 글자에 대해
                for next in range(cur+1, N):
                    # 현재값 + 거리^2값이 DP에 저장된 값보다 작다면 갱신
                    if string[next] == next_text and DP[cur] + (next-cur)**2 < DP[next]:
                        DP[next] = DP[cur] + (next-cur)**2

    # 마지막 결과값이 INF라면 -1 출력
    if DP[N-1] > 10e7:
        return -1
    else:
        return DP[N-1]


def main():
    N = int(input())
    string = input().rstrip()

    print(solve(N, string))


main()
