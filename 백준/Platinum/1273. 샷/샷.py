# 백준 1273

'''
높이를 기준으로 세그먼트 트리를 생성한다.
각 노드는 [자식 노드에 공기총을 맞지 않은 층의 수]를 저장한다. (맞은 경우 0, 맞지 않은 경우 1)

q번째 층에 공기총을 쐈다고 가정할 때, 이전 공기총 발사로 인해 q번째 층이 초기 위치가 아닐 수 있으므로,
세그먼트 트리로 q번째 층의 인덱스를 구해서 처리하도록 한다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
MAX = 1048576       # 10^6을 넘는 2의 제곱수 중 최소값


# num이상의 2의 제곱수 반환
def square(num):
    result = 1
    while True:
        if result >= num:
            return result
        result *= 2


# 누적합을 이용한 score 전처리
def setScore(N, black, gray, white):
    score = [0 for _ in range(MAX)]

    for i in range(N):
        acc = 0
        score[acc] += 1
        score[acc+black[i]] -= 1

        acc += black[i]
        score[acc] += 2
        score[acc+gray[i]] -= 2

        acc += gray[i]
        score[acc] += 5
        score[acc+white[i]] -= 5

    for i in range(1, MAX):
        score[i] += score[i-1]
    
    return [0] + score


# num이상의 2의 제곱수 반환
def square(num):
    result = 1
    while True:
        if result >= num:
            return result
        result *= 2


# 세그먼트 트리 초기 설정
def init(N, tree):
    for i in range(N-1, 0, -1):
        tree[i] = tree[i<<1] + tree[i<<1 | 1]


# 초기 위치가 index인 층의 값을 value로 변경하는 연산
def update(N, tree, index, value):
    index += N
    tree[index] += value
    
    while index > 1:
        index >>= 1
        tree[index] = tree[index<<1] + tree[index<<1 | 1]


# num번째 값이 저장된 인덱스 반환
def query(N, tree, num):
    start = 1

    curIndex = 1
    while True:
        tree[curIndex] -= 1

        # 리프 노드에 도달한 경우
        if curIndex<<1 | 1 > N*2:
            break

        # 왼쪽 자식 노드에 해당 값이 있는 경우
        if start <= num < start+tree[curIndex<<1]:
            curIndex = curIndex<<1

        # 오른쪽 자식 노드에 해당 값이 있는 경우
        else:
            start = start+tree[curIndex<<1]
            curIndex = curIndex<<1 | 1
    
    return curIndex-N


# main 함수 ----------
N = int(input())

black = list(map(int, input().split()))
gray = list(map(int, input().split()))
white = list(map(int, input().split()))
for i in range(N):
    MAX = max(MAX, black[i]+gray[i]+white[i])
MAX = square(MAX)

# score 전처리
score = setScore(N, black, gray, white)

# 세그먼트 트리 설정
tree = [1 for _ in range(MAX*2)]
tree[MAX] = 0 
init(MAX, tree)

# 쿼리 처리
M = int(input())
for q in list(map(int, input().split())):
    index = query(MAX, tree, q)     # q번째 층의 인덱스(index) 반환
    print(score[index])     # index 층의 점수 출력
    update(MAX, tree, index, 0)     # index 층 파괴 처리