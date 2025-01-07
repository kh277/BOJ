# 백준 33071

'''
b를 key, a를 value로 dict에 저장한 뒤
이분 탐색으로 합이 K가 되는 두 쌍를 찾는다.
그 뒤, 이 두 쌍이 다른 value를 갖는지 체크하면 된다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**10


# mid와 curSum의 합이 K 이하인지 체크
def check(curIndex, mid):
    return True if mid + curIndex <= K else False


# dic[p] != dic[q]인 쌍이 존재하는지 체크
def checkSet(p, q):
    pSet = dic[p]
    qSet = dic[q]

    if len(pSet)*len(qSet) - len(pSet & qSet) > 0:
        return True
    
    return False


def solve():
    numB.sort()
    result = -INF

    # numB[curIndex]과 더해서 합이 K 이하가 되는 수 중 최대값 찾기
    for curIndex in range(len(numB)):
        start = 0
        end = len(numB)-1

        # 이분 탐색
        while end - start > 1:
            mid = (end + start) // 2

            if check(numB[mid], numB[curIndex]) == True:
                start = mid
            else:
                end = mid
        
        # 종료 체크
        if check(numB[curIndex], numB[end]) == True and checkSet(numB[curIndex], numB[end]) == True:
            result = max(result, numB[curIndex]+numB[end])
        elif check(numB[curIndex], numB[start]) == True and checkSet(numB[curIndex], numB[start]) == True:
            result = max(result, numB[curIndex]+numB[start])

    if result == -INF:
        return 'NO'
    else:
        return result


# main 함수 ----------
N, K = map(int, input().split())
dic = dict()
numB = []
for _ in range(N):
    a, b = map(int, input().split())
    numB.append(b)
    if b in dic:
        dic[b].add(a)
    else:
        dic[b] = {a}

print(solve())