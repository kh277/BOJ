# 백준 12795

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
MAX = 10**13
INF = 10**30


class Line:
    __slots__ = ("a", "b")
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get(self, x):
        return self.a*x + self.b


# node가 관리하는 구간 [s, e]에 직선 v를 추가하기
def update(tree, node, v):
    s = tree[node][2]
    e = tree[node][3]
    m = (s + e) >> 1

    low = tree[node][4]
    high = v

    # 시작점에서 high가 위에 오도록 수정
    if low.get(s) > high.get(s):
        low, high = high, low

    # high가 시작점, 끝점 모두 위에 있는 경우
    if low.get(e) <= high.get(e):
        tree[node][4] = high
        return

    # 오른쪽 노드에서 low, high가 교차하는 경우
    if low.get(m) < high.get(m):
        tree[node][4] = high
        if tree[node][1] == -1:
            tree[node][1] = len(tree)
            tree.append([-1, -1, m+1, e, Line(0, -INF)])
        update(tree, tree[node][1], low)
    # 왼쪽 노드에서 low, high가 교차하는 경우
    else:
        tree[node][4] = low
        if tree[node][0] == -1:
            tree[node][0] = len(tree)
            tree.append([-1, -1, s, m, Line(0, -INF)])
        update(tree, tree[node][0], high)


# node가 관리하는 구간에서 함수값 x 구하기
def query(tree, node, x):
    # node가 아직 생성되지 않은 경우
    if node == -1:
        return -INF

    s = tree[node][2]
    e = tree[node][3]
    m = (s + e) >> 1

    # 자식 노드로 전이
    cur = tree[node][4].get(x)
    if x <= m:
        return max(cur, query(tree, tree[node][0], x))
    else:
        return max(cur, query(tree, tree[node][1], x))


def main():
    Q = int(input())
    tree = [[-1, -1, -MAX, MAX, Line(0, -INF)]]
    for _ in range(Q):
        q, *a = map(int, input().split())
        if q == 1:
            update(tree, 0, Line(a[0], a[1]))
        else:
            print(query(tree, 0, a[0]))


main()
