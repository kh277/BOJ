# 백준 15650번

import sys
input = sys.stdin.readline


class DFS:
    def __init__(self):
        # 결과를 저장할 리스트
        self.result = []

    def recur(self, N: int, M: int, cur: list):
        # 수열의 길이가 M에 도달할 경우 재귀 종료
        if len(cur) == M:
            self.result.append(cur)
            return cur

        # N, M, cur에 대한 정보를 가지고 재귀
        for i in range(1, N + 1):
            # 추가할 숫자가 이미 cur에 존재하는 경우 스킵
            if i in cur:
                continue
            # 추가할 숫자보다 큰 숫자가 이미 cur에 존재하는 경우 스킵
            if len(cur) != 0 and i < cur[-1]:
                continue
            self.recur(N, M, cur + [i])


def main():
    N, M = map(int, input().split())
    a = DFS()
    a.recur(N, M, [])
    for i in a.result:
        print(*i)


main()
