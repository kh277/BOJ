# 백준 15650번

import sys
input = sys.stdin.readline


class DFS:
    def __init__(self, num: list):
        # 결과를 저장할 리스트
        self.result = []
        self.num = sorted(num)

    def recur(self, N: int, M: int, cur: list):
        # 수열의 길이가 M에 도달할 경우 재귀 종료
        if len(cur) == M:
            self.result.append(cur)
            return cur

        # N, M, cur에 대한 정보를 가지고 재귀
        for i in range(N):
            # 추가할 숫자가 이미 cur에 존재하는 경우 스킵
            if self.num[i] in cur:
                continue

            self.recur(N, M, cur + [self.num[i]])


def main():
    N, M = map(int, input().split())
    num = list(map(int, input().split()))
    a = DFS(num)
    a.recur(N, M, [])
    for i in a.result:
        print(*i)


main()
