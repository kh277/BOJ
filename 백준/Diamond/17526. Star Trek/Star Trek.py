# 백준 17526

MAX = 10**13
INF = 1<<63


class Line:
    __slots__ = ("a", "b")
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get(self, x):
        return self.a*x + self.b


def build():
    return [[-1, -1, -MAX, MAX, Line(0, -INF)]]


# index번 노드가 관리하는 구간 [s, e]에 직선 v를 추가하기
def update(tree, index, v):
    newLine = v
    curI = index

    while True:
        start = tree[curI][2]
        end = tree[curI][3]
        mid = (start + end) >> 1

        low = tree[curI][4]
        high = newLine

        if low.get(start) > high.get(start):
            low, high = high, low

        if low.get(end) <= high.get(end):
            tree[curI][4] = high
            return

        if start == end:
            return

        if low.get(mid) < high.get(mid):
            tree[curI][4] = high
            newLine = low
            nextI = tree[curI][1]
            if nextI == -1:
                nextI = len(tree)
                tree[curI][1] = nextI
                tree.append([-1, -1, mid+1, end, Line(0, -INF)])
                tree[nextI][4] = newLine
                return
            curI = nextI
        else:
            tree[curI][4] = low
            newLine = high
            nextI = tree[curI][0]
            if nextI == -1:
                nextI = len(tree)
                tree[curI][0] = nextI
                tree.append([-1, -1, start, mid, Line(0, -INF)])
                tree[nextI][4] = newLine
                return
            curI = nextI


# index번 노드가 관리하는 구간에서 함수값 x 구하기
def query(tree, index, x):
    curI = index
    result = -INF

    while curI != -1:
        start = tree[curI][2]
        end = tree[curI][3]
        mid = (start + end) >> 1
        value = tree[curI][4].get(x)
        if value > result:
            result = value

        if start == end:
            break

        if x <= mid:
            curI = tree[curI][0]
        else:
            curI = tree[curI][1]

    return result


def solve(N, gap, wait, speed):
    x = [0] * (N+2)
    for i in range(2, N+1):
        x[i] = x[i-1] + gap[i-2]

    tree = build()
    update(tree, 0, Line(-speed[1], -wait[1]))

    for i in range(2, N):
        a = -query(tree, 0, x[i])
        b = wait[i] + a - speed[i]*x[i]
        update(tree, 0, Line(-speed[i], -b))

    return -query(tree, 0, x[N])


def main():
    N = int(input())
    gap = list(map(int, input().split()))
    wait = [0]
    speed = [0]
    for _ in range(N-1):
        w, s = map(int, input().split())
        wait.append(w)
        speed.append(s)

    print(solve(N, gap, wait, speed))


main()
