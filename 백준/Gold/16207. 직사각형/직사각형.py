# 백준 16207

'''
직사각형의 넓이는 가로, 세로가 길어질수록 넓이가 넓어지므로,
그리디하게 길이가 가장 긴 선분 4개부터 탐색을 시작한다..

우선, 선분을 길이 내림차순으로 정렬한다.
0, 1번째 인덱스의 선분을 적절하게 조절하여
직사각형의 한 변을 만들 수 있으면 다음 탐색은 2, 3번 인덱스의 선분을 탐색하고,
직사각형을 만들 수 없으면 다음 탐색은 1, 2번째 인덱스의 선분을 탐색한다.

위와 같은 방법으로 끝까지 탐색을 하면 된다.
'''

import sys

input = sys.stdin.readline


def solve(N: int, stick: list) -> int:
    # 직사각형 자체를 만들 수 없는 경우
    if N <= 3:
        return 0
    
    # 내림차순 정렬
    stick.sort(reverse=True)
    
    # 선분 2개로 직사각형을 만들 수 있는지 판단
    line = []
    index = 0
    while index < N-1:
        cur = [stick[index], stick[index+1]]
        
        if cur[0] - cur[1] == 0:
            line.append(cur[0])
        elif cur[0] - cur[1] == 1:
            line.append(cur[1])
        else:
            # 해당 index로는 선분을 만들 수 없으므로 +1
            index += 1
            continue
        
        # 선분 2개를 사용했으므로 +2
        index += 2
        
    # 직사각형을 만들 수 있는 경우
    result = 0
    for i in range(0, len(line)-1, 2):
        result += line[i] * line[i+1]
    
    return result


def main():
    N = int(input())
    stick = list(map(int, input().split()))
    
    print(solve(N, stick))
    

main()