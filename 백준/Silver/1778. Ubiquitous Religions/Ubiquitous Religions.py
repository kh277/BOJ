# 백준 1778

import sys

input = sys.stdin.readline


# x의 루트 정점을 탐색
def find(parent, x) -> int:
    if parent[x] != x:
        parent[x] = find(parent, parent[x])

    return parent[x]


# a 트리와 b 트리 병합
def union(parent, a, b) -> None:
    a = find(parent, a)
    b = find(parent, b)
		
		# 높이가 낮은 트리를 
    if a != b:
        parent[b] = a
    else:
        parent[a] = b


def solve(case):
    parent = [i for i in range(V)]
    for a, b in data:
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
    
    # 부모 정점이 두 번에 걸쳐 갱신될 수도 있으므로 한번 더 반복
    for a, b in data:
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
    
    return "Case {a}: {b}".format(a=case, b=len(set(parent)))


# main 함수 ----------
case = 1
while True:
    V, E = map(int, input().split())
    if V == 0 and E == 0:
        break

    data = []
    for _ in range(E):
        a, b = map(int, input().split())
        data.append([a-1, b-1])

    print(solve(case))
    case += 1