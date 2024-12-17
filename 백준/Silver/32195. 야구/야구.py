# 백준 32195

import io

input = io.BufferedReader(io.FileIO(0), 1 << 18).readline


# 파울 여부 체크
def checkFoul(x, y):
    if y >= x and y >= -x:
        return True
    else:
        return False


# 파울 여부를 확인하여 점까지의 거리를 반환
def update(point, inside, foul):
    if checkFoul(point[0], point[1]) == True:
        inside.append(point[0]**2 + point[1]**2)
    else:
        foul += 1
    
    return inside, foul


# 반지름 R 내에 존재하는지 체크
def checkRange(curRange, R):
    if curRange <= R**2:
        return True
    else:
        return False


# R 이내의 타구 개수 반환
def query(R, inside, foul):
    start = 0
    end = len(inside)-1

    # 이분 탐색
    while end - start > 1:
        mid = (end + start) // 2

        if checkRange(inside[mid], R) == False:
            end = mid-1
        else:
            start = mid

    # 마지막 범위 체크
    if checkRange(inside[end], R) == True:
        return [foul, end+1, len(inside)-end-1]
    elif checkRange(inside[start], R) == True:
        return [foul, start+1, len(inside)-start-1]
    else:
        return [foul, 0, len(inside)]


# main 함수 ----------
N = int(input())
point = []
inside = []
foul = 0

# 입력 처리
for _ in range(N):
    inside, foul = update(list(map(int, input().split())), inside, foul)

# 쿼리 처리
inside.sort()
Q = int(input())
for _ in range(Q):
    candidate = int(input())
    print(*query(candidate, inside, foul))
