# 백준 1497

'''
비트마스킹 + 브루트포스를 사용한 풀이
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 100


# 방문(0), 미방문(1) 표시
def changeBit(M, string):
    result = 0
    for i in range(M):
        if string[i] == 'Y':
            result = result | (1<<i)

    return result


def solve(N, M, data):
    resultSong = -1
    resultGuitar = INF

    # 기타를 살 수 있는 모든 경우 처리
    for curStatus in range((1<<N)):
        # 현재 상태에서 사용된 기타의 수 체크 및 곡의 수 비트마스킹
        curGuitar = 0
        songMask = 0
        for i in range(N):
            if curStatus & (1<<i) != 0:
                songMask = songMask | data[i]
                curGuitar += 1

        # 곡의 수 체크
        curSong = 0
        for i in range(M):
            if songMask & (1<<i) != 0:
                curSong += 1

        # 더 많은 곡을 연주할 수 있다면
        if curSong > resultSong:
            resultSong = curSong
            resultGuitar = curGuitar
        # 연주할 수 있는 곡의 수가 같다면
        elif curSong == resultSong:
            resultGuitar = min(resultGuitar, curGuitar)

    return resultGuitar if resultGuitar != 0 else -1


def main():
    N, M = map(int, input().split())
    data = []
    for _ in range(N):
        _, b = map(str, input().decode().split())
        data.append(changeBit(M, b))

    print(solve(N, M, data))


main()
