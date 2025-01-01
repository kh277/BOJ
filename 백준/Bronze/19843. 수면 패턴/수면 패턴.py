# 백준 19843

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
month = {'Mon':0, 'Tue':1, 'Wed':2, 'Thu':3, 'Fri':4}


def solve():
    result = 0
    for cur in range(M):
        result += month[time[cur][2]]*24 + int(time[cur][3]) - (month[time[cur][0]]*24 + int(time[cur][1]))

    return -1 if N-result > 48 else max(N-result, 0)


# main 함수 ----------
N, M = map(int, input().split())
time = []
for _ in range(M):
    time.append(list(map(str, input().rstrip().decode().split())))

print(solve())
