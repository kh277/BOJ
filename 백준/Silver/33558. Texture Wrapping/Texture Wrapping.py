# C번

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, M, U, V, data, wrapType):
    result = [['0' for _ in range(M)] for _ in range(N)]

    # 1번 케이스
    if wrapType == 'clamp-to-edge':
        # 기본 텍스쳐
        for y in range(min(N, U)):
            for x in range(min(M, V)):
                result[y][x] = data[y][x]
        
        # 가로 확장
        for y in range(min(N, U)):
            for x in range(V, M):
                result[y][x] = data[y][V-1]
        
        # 세로 확장
        for y in range(U, N):
            for x in range(min(M, V)):
                result[y][x] = data[U-1][x]
        
        # 대각선 확장
        for y in range(U, N):
            for x in range(V, M):
                result[y][x] = data[U-1][V-1]

    # 2번 케이스
    elif wrapType == 'repeat':
        for y in range(N):
            for x in range(M):
                result[y][x] = data[y%U][x%V]

    # 3번 케이스
    else:
        for y in range(N):
            for x in range(M):
                # 반전 처리
                if y//U % 2 == 0 and x//V % 2 == 0:
                    result[y][x] = data[y%U][x%V]
                elif y//U % 2 == 1 and x//V % 2 == 0:
                    result[y][x] = data[(U-1)-y%U][x%V]
                elif y//U % 2 == 0 and x//V % 2 == 1:
                    result[y][x] = data[y%U][(V-1)-x%V]
                else:
                    result[y][x] = data[(U-1)-y%U][(V-1)-x%V]
    
    return [''.join(x) for x in result]


def main():
    N, M = map(int, input().split())
    U, V = map(int, input().split())
    data = []
    for _ in range(U):
        data.append(list(map(str, input().decode().strip())))
    wrapType = input().decode().rstrip()
    for i in solve(N, M, U, V, data, wrapType):
        print(i)


main()