# 백준 30681

'''
캘리퍼스를 회전시킬 때, 기준 선분에 대해 CCW의 값이 가장 큰 점을 발견할 경우,
기준 선분의 끝점부터 최대 점까지 선분으로 이은 길이를 계산한다.
만약 가장 큰 점이 2개(두 캘리퍼스가 평행)인 경우, 기준 선분도 길이에 포함시킨다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**8


def CCW(A, B, C):
    return (B[0]-A[0]) * (C[1]-A[1]) - (B[1]-A[1]) * (C[0]-A[0])


def distance(A, B):
    return ((A[0]-B[0])**2 + (A[1]-B[1])**2)**0.5


# start번째 점 ~ end번째 점까지 선분으로 전부 이을 때의 총 길이 반환
def getLength(N, accLength, start, end, clockWise):
    if start > end:
        end += N

    if clockWise == 1:
        return accLength[end] - accLength[start]
    else:
        return accLength[N]-accLength[end] + accLength[start]    


def ConvexHull(points):
    points = sorted(set(points))

    lower = []
    for point in points:
        while len(lower) >= 2 and CCW(lower[-2], lower[-1], point) <= 0:
            lower.pop()
        lower.append(point)

    upper = []
    for point in reversed(points):
        while len(upper) >= 2 and CCW(upper[-2], upper[-1], point) <= 0:
            upper.pop()
        upper.append(point)

    return lower[:-1] + upper[:-1]


def RotatingCalipers(points):
    # 볼록 껍질 도출
    hull = ConvexHull(points)
    length = len(hull)

    # 0번 점으로부터의 둘레 누적합 미리 계산
    accLength = [0 for _ in range(length*2)]
    for cur in range(1, length+1):
        accLength[cur] = distance(hull[cur-1], hull[cur%length]) + accLength[cur-1]
    for cur in range(length+1, length*2):
        accLength[cur] = distance(hull[(cur-1)%length], hull[cur%length]) + accLength[cur-1]

    # 특수 케이스 처리
    if length < 2:
        return 0
    elif length == 2:
        return distance(hull[0], hull[1])
    
    result = INF
    curFarestP = 1
    for curP in range(length):
        nextP = (curP+1) % length

        # 선분 curP nextP와 가장 큰 CCW를 가진 점 도출
        while True:
            nextFarestP = (curFarestP+1) % length
            d1 = CCW(hull[curP], hull[nextP], hull[curFarestP])
            d2 = CCW(hull[curP], hull[nextP], hull[nextFarestP])

            # 평행 대칭점을 찾은 경우 -> 기준 선분을 결과에 포함시키기
            if d1 == d2:
                result = min(result, getLength(length, accLength, curP, curFarestP, 1))
                result = min(result, getLength(length, accLength, nextP, nextFarestP, -1))
                curFarestP = nextFarestP
            # 더 큰 CCW값이 존재하는 경우 -> curFarestP 이동
            elif d1 < d2:
                curFarestP = nextFarestP
            # 평행이 아닌 대칭점을 찾은 경우 -> 결과 저장
            else:
                result = min(result, getLength(length, accLength, nextP, curFarestP, 1))
                break

    return result


def main():
    N = int(input())
    points = []
    for _ in range(N):
        points.append(tuple(map(int, input().split())))
    
    print(RotatingCalipers(points))


main()
