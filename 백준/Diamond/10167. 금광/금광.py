# 백준 10167

'''
1. 좌표 압축
2. y좌표 시작점과 끝점을 N^2으로 돌면서 범위 설정
3. 2에서 정해진 범위에 속하는 점들에 대해 최대 연속합 구하기

세그먼트 트리의 각 노드에는 [구간의 왼쪽 접두사 포함 최대 연속합,
구간의 오른쪽 접미사 포함 최대 연속합, 구간 내 최대 연속합, 구간 내 총합] 저장.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**13


def square(num):
    result = 1
    while True:
        if result >= num:
            return result
        result *= 2


# axis 좌표축에 대해 압축
def compress(N, point, axis):
    point.sort(key= lambda x: x[axis])
    before = point[0][axis]
    curPos = 0
    for i in range(N):
        if point[i][axis] == before:
            point[i][axis] = curPos
        else:
            before = point[i][axis]
            curPos += 1
            point[i][axis] = curPos

    return curPos, point


# left노드 + right노드에서 최대 연속합 노드 처리 
def combine(leftNode, rightNode):
    return [max(leftNode[0], leftNode[3]+rightNode[0]),
            max(rightNode[1], leftNode[1]+rightNode[3]),
            max(leftNode[2], rightNode[2], leftNode[1]+rightNode[0]),
            leftNode[3] + rightNode[3]]


# 세그먼트 트리 구성
def init(N, tree):
    for i in range(N-1, 0, -1):
        left = i<<1
        right = i<<1 | 1

        tree[i] = combine(tree[left], tree[right])


def solve(N, point):
    # 1. x, y좌표 압축
    maxX, point = compress(N, point, 0)
    maxY, point = compress(N, point, 1)

    # y좌표 시작지점 저장
    point.sort(key= lambda x: (x[1], x[0]))
    startIndexY = [N for _ in range(maxY+2)]
    index = 0
    for i in range(N):
        if startIndexY[index] == N and point[i][1] == index:
            startIndexY[index] = i
            index += 1

    treeSize = square(maxX+1)
    result = -INF

    # 2. 시작점과 끝점 범위 설정
    for startY in range(maxY+1):
        beforeY = startY

        tree = [[0, 0, 0, 0] for _ in range(treeSize*2)]
        for endY in range(startY, maxY+1):
            # y좌표가 구간 [beforeY, endY]에 속하는 점들의 개발 이익를 세그먼트 트리에 추가
            for i in range(startIndexY[beforeY], startIndexY[endY+1]):
                for j in range(4):
                    tree[point[i][0]+treeSize][j] += point[i][2]

            # 3. y좌표가 구간 [startY, endY]에 속하는 점들에 대해 최대 연속합 구하기
            init(treeSize, tree)
            result = max(result, tree[1][2])

            beforeY = endY+1

    return result


def main():
    N = int(input())
    point = []
    for _ in range(N):
        point.append(list(map(int, input().split())))
    print(solve(N, point))


main()
