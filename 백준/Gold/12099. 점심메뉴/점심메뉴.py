# 백준 12099

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def check(arrNum, findData):
    if arrNum >= findData:
        return True

    return False


# menu에서 findData가 들어갈 수 있는 상한 반환
def BinarySearch(menu, findData):
    start = 0
    end = len(menu)-1

    while end - start > 1:
        mid = (start+end)//2
        if check(menu[mid][0], findData) == False:
            start = mid+1
        else:
            end = mid
    
    if check(menu[start][0], findData) == True:
        return start
    elif check(menu[end][0], findData) == True:
        return end
    else:
        return end+1


def solve(menu, u, v, x, y):
    # 매운맛 조건을 만족하는 메뉴의 범위를 이분 탐색으로 찾기
    start = BinarySearch(menu, u)
    end = BinarySearch(menu, v+1)

    # 단맛 조건을 만족하는 메뉴의 범위를 브루트포스로 찾기
    result = 0
    for cur in range(start, end):
        if x <= menu[cur][1] <= y:
            result += 1

    return result


def main():
    N, Q = map(int, input().split())
    menu = []
    for _ in range(N):
        menu.append(list(map(int, input().split())))
    menu.sort(key= lambda x:(x[0]))

    for _ in range(Q):
        u, v, x, y = map(int, input().split())
        print(solve(menu, u, v, x, y))


main()
