# 백준 17126

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


# 값 압축 함수
def compress(value):
    comp = dict()
    value.sort()
    compress = 0
    comp[value[0]] = 0
    for i in range(1, len(value)):
        if value[i-1] != value[i]:
            compress += 1
        comp[value[i]] = compress

    return comp


# index번째 값에 value만큼 추가하는 쿼리
def update(N, tree, index, value=None):
    index += N
    if value == None:
        tree[index] = 0
    else:
        tree[index] += value
    
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


def main():
    N = int(input())

    # 쿼리 저장
    q = []
    value = []
    for _ in range(N):
        a, *b = map(int, input().split())
        q.append([a, *b])
        if a == 1:
            value.append(b[0])
        elif a == 2:
            value.append(b[0])
            value.append(b[1])
        else:
            value.append(b[0])

    # 값 압축
    comp = compress(value)

    # 쿼리 처리
    size = 1 << (comp[value[-1]]).bit_length()
    tree = [0 for _ in range(size*2)]
    for i in range(N):
        if q[i][0] == 1:
            update(size, tree, comp[q[i][1]], q[i][2])
            print(tree[1], end=" ")
        elif q[i][0] == 2:
            print(query(size, tree, comp[q[i][1]], comp[q[i][2]]), end=" ")
        else:
            update(size, tree, comp[q[i][1]])
            print(tree[1], end=" ")


main()
