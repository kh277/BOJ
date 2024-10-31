# 백준 2672

'''
스위핑을 통해 y축을 왼쪽에서 오른쪽으로 이동시키면서 넓이를 구하자.
'''

import sys

input = sys.stdin.readline
LIMIT = 10000

def sweep(startX):
    rangeY = [0 for _ in range(LIMIT*2+1)]

    for i in range(N):
        # 현재 탐색 범위 내에 사각형이 존재하는지 확인
        if square[i][0] <= startX and square[i][1] > startX:
            for y in range(square[i][2], square[i][3]):
                rangeY[y] = 1
    
    # y좌표에서 1의 개수 체크
    result = 0
    for i in range(LIMIT*2+1):
        if rangeY[i] == 1:
            result += 1

    return result


def solve():
    # y축을 왼쪽에서 오른쪽으로 스위핑할 때, 사각형과 만나는 곳이 달라지는 구간 체크
    pointX = set()
    for i in range(N):
        pointX.add(square[i][0])
        pointX.add(square[i][1])
    
    # 사각형이 존재하는 y범위를 구하고 사각형 넓이 구하기
    endX = sorted(list(pointX))
    result = 0
    for i in range(len(endX)-1):
        # startX ~ endX 범위에서 사각형의 y좌표의 길이를 구해서 곱하기 
        result += sweep(endX[i]) * (endX[i+1]-endX[i])
    
    # 출력 결과 소수점 처리
    final = round(result/100, 2)
    if final.is_integer():
        return str(int(final))
    else:
        return f"{final:.2f}"


# main 함수 ----------
N = int(input())
square = []
for _ in range(N):
    x, y, w, h = map(float, input().split())
    # [좌하단x, 우상단x, 좌하단y, 우상단y] 순서로 저장
    square.append(list([int(x*10), int(x*10)+int(w*10), int(y*10), int(y*10)+int(h*10)]))

print(solve())
