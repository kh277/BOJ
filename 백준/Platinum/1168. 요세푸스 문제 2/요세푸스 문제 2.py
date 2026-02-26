# 백준 1168

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


# 크기가 N인 세그먼트 트리 빌드
def build(N, size):
    tree = [0] * (size*2)
    for i in range(N):
        tree[size+i] = 1
    for i in range(size-1, 0, -1):
        tree[i] = tree[i<<1] + tree[i<<1 | 1]

    return tree


# index번째 값을 value로 변경
def update(N, tree, index, value):
    index += N
    tree[index] = value

    while index > 1:
        index >>= 1
        tree[index] = tree[index<<1] + tree[index<<1 | 1]


# 구간 [left, right]의 전체 합을 구하는 쿼리
def query(N, tree, left, right):
    result = 0
    left += N
    right += N

    while left <= right:
        if left & 1:
            result += tree[left]
            left += 1
        if ~right & 1:
            result += tree[right]
            right -= 1
        left >>= 1
        right >>= 1

    return result


# 앞에서부터 target번째에 존재하는 수의 인덱스 반환
def getKth(N, tree, target):
    curV = 1
    while curV < N:
        left = curV<<1
        right = curV<<1 | 1
        if tree[left] < target:
            curV = right
            target -= tree[left]
        else:
            curV = left

    return curV - N


def main():
    N, K = map(int, input().split())

    size = 1<<(N-1).bit_length()
    tree = build(N, size)
    curI = 0
    out = ["<"]

    for _ in range(N):
        # 구간 [0, curPos-1]에 존재하는 수의 개수 처리
        prev = 0
        if curI != 0:
            prev = query(size, tree, 0, curI)

        # curI부터 K번 뒤의 수의 인덱스 반환
        target = (prev + K - 1) % tree[1] + 1
        index = getKth(size, tree, target)
        out.append(str(index+1))
        out.append(", ")

        # 해당 인덱스의 숫자 제거
        update(size, tree, index, 0)
        curI = index

    # 결과 포매팅
    out.pop()
    out.append(">")
    print("".join(out))


main()
