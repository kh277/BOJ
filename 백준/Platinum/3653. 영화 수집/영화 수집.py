# 백준 3653

'''
각 영화가 세그먼트 트리 리프 노드의 어느 인덱스에 있는지를 저장하는 배열(pos)을 이용한다.

i번 영화를 꺼낼 경우 위의 영화들은 위치를 전부 이동시켜야 하지만 이 처리가 힘들다.
그래서 영화를 꺼낼 경우 해당 위치를 0으로 처리하고 가장 뒷부분에 추가해준다.
ex) 654321 -> 6503214
이 경우 쿼리 한번 당 필요한 길이가 한 칸씩 증가되므로 총 n+m만큼의 배열이 필요하다.

따라서 DVD의 개수 + 쿼리 개수를 기준으로 세그먼트 트리를 생성하고,
각 노드는 [자식 노드에 저장된 영화 개수의 합]를 저장한다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


# 세그먼트 트리 구성
def init(N, tree):
    for i in range(N-1, 0, -1):
        tree[i] = tree[i<<1] + tree[i<<1 | 1]


# tree[index]을 value으로 값 변경, 트리 갱신
def update(N, tree, index, value):
    index += N
    tree[index] = value
    
    while index > 1:
        index >>= 1
        tree[index] = tree[index<<1] + tree[index<<1 | 1]


# 구간 [left, right]에서 리프 노드의 총합 반환
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


# main 함수 ----------
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())

    # 세그먼트 트리 기본 설정
    pos = [i for i in range(N, -1, -1)]
    tree = [0 for _ in range(2*(N+M))]
    for i in range(N+M, 2*N+M):
        tree[i] = 1
    init(N+M, tree)

    # 쿼리 처리
    endPos = N
    for q in list(map(int, input().split())):
        curPos = pos[q]
        update(N+M, tree, pos[q], 0)        # q번 영화 꺼내기
        print(query(N+M, tree, pos[q], endPos), end=' ')     # 위에 쌓인 영화의 수 반환
        update(N+M, tree, endPos, 1)        # 끝에 추가
        pos[q] = endPos         # pos값 갱신
        endPos += 1
    print()