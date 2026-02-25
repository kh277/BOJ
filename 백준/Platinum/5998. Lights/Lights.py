# 백준 5998

'''
각 스위치에 의해 켜지는 전구 집합을 비트 상태로 표시한다.
그리고 스위치들을 두 부분으로 나누어 앞쪽 V개, 뒤쪽 V개에 대해 아래 과정을 처리한다.
스위치를 누를 수 있는 모든 조합의 수를 set에 스위치를 누른 횟수와 함께 저장해준다.
앞쪽 V개에 속한 어떤 조합 방법에서, 그 조합에 포함된 스위치를 전부 눌렀을 때의 전구 상태를 전부 뒤집은 상태가
뒤쪽 V개 조합에 포함되어 있다면 두 횟수를 더해준다.
이런 비트마스킹 + 중간에서 만나기 방법으로 스위치를 누르는 횟수의 최소값을 찾아주면 된다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 40


def getCombination(V, bulb, s, e):
    comb = set()
    dic = dict()
    for swtichStatus in range(1<<V):
        onBit = 0
        index = 0
        bulbStatus = 0
        while swtichStatus > 0:
            if swtichStatus & 1:
                bulbStatus ^= bulb[s+index]
                onBit += 1
            swtichStatus >>= 1
            index += 1
        if bulbStatus not in dic:
            dic[bulbStatus] = onBit
            comb.add(bulbStatus)

    return comb, dic


def solve(V, graph):
    # 스위치를 눌렀을 때 켜지는 전구 상태 저장
    bulb = []
    for curV in range(V):
        status = 1<<curV
        for nextV in graph[curV]:
            status |= 1<<nextV
        bulb.append(status)

    # 스위치를 두 부분으로 분할 후 각 부분에서 만들 수 있는 전구 조합 도출
    s1 = 0
    e1 = V//2
    s2 = V//2 + 1
    e2 = V-1
    comb1, dic1 = getCombination(e1+1, bulb, s1, e1)
    _, dic2 = getCombination(e2-s2+1, bulb, s2, e2)

    # 두 조합을 합쳐 comp를 만들 수 있는지 체크
    comp = (1<<V) - 1
    minCount = INF
    for status in comb1:
        negStatus = comp ^ status
        if negStatus in dic2:
            minCount = min(minCount, dic1[status] + dic2[negStatus])

    return minCount


def main():
    V, E = map(int, input().split())
    graph = [[] for _ in range(V)]
    for _ in range(E):
        s, e = map(int, input().split())
        graph[s-1].append(e-1)
        graph[e-1].append(s-1)
    print(solve(V, graph))


main()
