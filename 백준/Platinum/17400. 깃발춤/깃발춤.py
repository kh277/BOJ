# 백준 17400

'''
어차피 홀수 값과 짝수 값 차이의 절대값을 구해야 하므로, 홀수번째 값은 부호를 반전시켜 저장하면 된다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def build(N, A):
    tree = [0] * (2*N)
    for i in range(len(A)):
        if i % 2 == 0:
            tree[i+N] = A[i]
        else:
            tree[i+N] = -A[i]
    for i in range(N-1, 0, -1):
        tree[i] = tree[i<<1] + tree[i<<1 | 1]

    return tree


# 점 업데이트
def update(N, tree, index, value):
    index += N
    tree[index] += value

    while index > 1:
        index >>= 1
        tree[index] = tree[index<<1] + tree[index<<1 | 1]


# 구간 쿼리
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
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    size = 1<<N.bit_length()
    tree = build(size, A)

    for _ in range(Q):
        a, b, c = map(int, input().split())
        b -= 1
        if a == 1:
            c -= 1
            print(abs(query(size, tree, b, c)))
        elif b % 2 == 0:
            update(size, tree, b, c)
        else:
            update(size, tree, b, -c)


main()
