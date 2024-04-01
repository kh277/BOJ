# 백준 1708

'''
Convex lower 및 Andrew's monotone chain에 관련된 정보 찾기
'''

# 2차원 벡터의 외적값을 이용해 회전 방향 판별
def cross(a, b, c):
    # 양수(반시계), 0(일직선), 음수(시계)
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def convex_hull(graph):
    
    graph = sorted(set(graph))

    # 위쪽 Hull을 구함
    upper = []
    for i in reversed(graph):
        # 반시계 방향이 아닐 경우 마지막 점 제거
        while len(upper) >= 2 and cross(upper[-2], upper[-1], i) <= 0:
            upper.pop()
        upper.append(i)

    # 아래쪽 Hull을 구함
    lower = []
    for i in graph:
        # 반시계 방향이 아닐 경우 마지막 점 제거
        while len(lower) >= 2 and cross(lower[-2], lower[-1], i) <= 0:
            lower.pop()
        lower.append(i)
    
    # 위쪽 Hull과 아래쪽 Hull을 중복제거하여 합치기
    return lower[:-1] + upper[:-1]


def main():
    N = int(input())
    graph = []

    for i in range(N):
        a, b = map(int, input().split())
        graph.append((a, b))

    print(len(convex_hull(graph)))

main()
