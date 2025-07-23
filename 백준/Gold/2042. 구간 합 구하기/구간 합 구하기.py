# 백준 2042

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
ARRAY_TYPE = 'q'


class SegmentTree:
    # 크기가 N인 세그먼트 트리 빌드
    def __init__(self, N):
        self.size = N
        self.tree = array(ARRAY_TYPE, [0]) * (self.size*2)

        for i in range(N):
            self.tree[N+i] = int(input())

        for i in range(N-1, 0, -1):
            self.tree[i] = self.tree[i<<1] + self.tree[i<<1 | 1]


    # index번째 값을 value로 변경
    def update(self, index, value):
        index += self.size
        self.tree[index] = value
        
        while index > 1:
            index >>= 1
            self.tree[index] = self.tree[index<<1] + self.tree[index<<1 | 1]


    # 0-base, 구간 [left, right]의 전체 합을 구하는 쿼리
    def query(self, left, right):
        result = 0
        left += self.size
        right += self.size

        while left <= right:
            if left & 1:
                result += self.tree[left]
                left += 1
            if ~right & 1:
                result += self.tree[right]
                right -= 1
            left >>= 1
            right >>= 1

        return result


def main():
    N, M, K = map(int, input().split())

    # 세그먼트 트리 설정
    t = SegmentTree(N)

    # 쿼리 입력 및 처리
    for _ in range(M+K):
        x, y, z = map(int, input().split())
        if x == 1:
            t.update(y-1, z)
        else:
            print(t.query(y-1, z-1))


main()
