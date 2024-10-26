# 백준 5676

import sys

input = sys.stdin.readline


# 세그먼트 트리 구성
def init(tree):
    for i in range(N-1, 0, -1):
        tree[i] = tree[i<<1] * tree[i<<1 | 1]


# index번째 인덱스를 value로 변경
def update(tree, index, value):
    index += N
    tree[index] = value
    
    while index > 1:
        index >>= 1
        tree[index] = tree[index<<1] * tree[index<<1 | 1]


# left ~ right까지의 쿼리 처리
def query(tree, left, right):
    result = 1
    left += N
    right += N
    
    while left <= right:
        # left가 홀수라면
        if left & 1:
            result = result * tree[left]
            left += 1
        # right가 홀수라면
        if ~right & 1:
            result = result * tree[right]
            right -= 1
            
        left >>= 1
        right >>= 1
    
    return result


# 입력받은 수를 1, -1, 0으로 변환
def change(L):
    result = []
    for i in L:
        if i > 0:
            result.append(1)
        elif i < 0:
            result.append(-1)
        else:
            result.append(0)

    return result


# main 함수 ----------
while True:
    try:
        N, K = map(int, input().split())
        X = change(list(map(int, input().split())))
        # 세그먼트 트리 설정
        tree = [0 for _ in range(2*N)]
        for i in range(N):
            tree[i+N] = X[i]
        init(tree)
        
        # 쿼리 입력 및 처리
        result = ""
        for _ in range(K):
            c, i, j = map(str, input().split())
            if c == 'C':
                if int(j) > 0:
                    j = 1
                elif int(j) < 0:
                    j = -1
                else:
                    j = 0
                update(tree, int(i)-1, j)
            else:
                answer = query(tree, int(i)-1, int(j)-1)
                if answer > 0:
                    result += '+'
                elif answer < 0:
                    result += '-'
                else:
                    result += '0'
        print(result)
    except:
        break
