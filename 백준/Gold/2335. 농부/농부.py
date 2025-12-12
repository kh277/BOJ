# 백준 2335

'''
무조건 정원을 선택하는 것이 이득이므로 Q에 가깝게 정원을 최대한 선택하고,
남은 나무의 수만큼 선택하지 않은 정원과 이랑에서 그리디하게 선택하면 된다.
DP[i] = 정원 중 일부를 선택해 정확히 i그루를 만들 수 있는가?
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(Q, M, tree, line):
    # DP로 나무 제한 Q를 넘지 않는 최대 나무 수 계산
    DP = [0] * (Q+1)
    prevSum = [-1] * (Q+1)
    prevIdx = [-1] * (Q+1)
    DP[0] = 1
    for i in range(M):
        curW = tree[i]
        for j in range(Q, curW-1, -1):
            if DP[j] == 0 and DP[j-curW] == 1:
                DP[j] = 1
                prevSum[j] = j-curW
                prevIdx[j] = i

    # 정원을 선택하고 남은 나무의 수 계산
    olive = 0
    leftTree = Q
    for i in range(Q, -1, -1):
        if DP[i] == 1:
            olive += i
            leftTree -= i
            break

    # 선택한 정원 역추적
    use = set()
    cur = Q - leftTree
    while cur != 0:
        curI = prevIdx[cur]
        use.add(curI)
        cur = prevSum[cur]

    # 선택되지 않은 정원 이랑에 추가
    for i in range(M):
        if i not in use:
            line.append(tree[i])

    # 남은 정원과 이랑에서 그리디하게 선택
    if leftTree > 0:
        line.sort(reverse=True)
        for curL in line:
            if curL < leftTree:
                leftTree -= curL
                olive += curL-1
            else:
                olive += leftTree-1
                break

    return olive


def main():
    Q, M, K = map(int, input().split())
    tree = list(map(int, input().split()))
    line = list(map(int, input().split()))
    print(solve(Q, M, tree, line))


main()
