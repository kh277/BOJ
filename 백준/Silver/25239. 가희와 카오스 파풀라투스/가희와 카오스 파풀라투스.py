# 백준 25239


import sys

input = sys.stdin.readline


def solve():
    curTime = start[0]*60 + start[1]
    activate = [1 for _ in range(6)]
    
    for i in range(Q):
        time, ask = query[i]
        # 차원의 균열 패턴이 끝난 경우
        if float(time) > 60:
            return min(sum([area[i]*activate[i] for i in range(6) if activate[i] == 1]), 100)
        
        # 포탈에서 윗키를 누른 경우
        if ask[-1] == '^':
            for i in range(6):
                if 120*i < curTime < 120*(i+1):
                    activate[i] = 0
                    break
            
            # 모든 칸이 봉인된 경우
            if sum(activate) == 6:
                return 0
        
        # +시간을 먹은 경우
        elif ask[-1] == 'R':
            curTime = (curTime + int(ask[0])*60) % 720
        
        # +분을 먹은 경우
        else:
            curTime = (curTime + int(ask[:2])) % 720
    
    return min(sum([area[i]*activate[i] for i in range(6) if activate[i] == 1]), 100)


# main 함수 ----------
start = list(map(int, input().split(':')))
area = list(map(int, input().split()))

Q = int(input())
query = []
for _ in range(Q):
    query.append(input().rstrip().split())
    
print(solve())