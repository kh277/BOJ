# 백준 16226

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, data):
    pos = dict()    
    for y, x in data:
        # 거울냥이 추가 (x좌표, 거울 여부(0))
        if y not in pos:
            pos[y] = [(x, 0)]
        else:
            pos[y].append((x, 0))

        # 거울 추가 (x좌표, 거울 여부(1))
        if y+1 not in pos:
            pos[y+1] = [(x, 1)]
        else:
            pos[y+1].append((x, 1))

    # 각 줄별로 거울냥이가 존재하는지 체크
    result = 0
    for curY in pos.keys():
        curData = pos[curY]
        curData.sort()

        isCat = 0
        for _, isMirror in curData:
            # 현재 칸이 거울일 경우
            if isMirror == 1:
                if isCat == 1:
                    result += 1
                isCat = 0
            # 현재 칸이 거울냥이일 경우
            else:
                isCat = 1

        if isCat == 1:
            result += 1

    return result


def main():
    N = int(input())
    data = []
    for _ in range(N):
        data.append(list(map(int, input().split())))
    print(solve(N, data))


main()
