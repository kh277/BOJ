# 백준 33562

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def cutter(diagram):
    if diagram == None:
        return [None, None]

    # 절단 작업
    result = [[], []]
    diagram = list(map(str, diagram.split(":")))
    for i in range(len(diagram)):
        left = diagram[i][:4] + "----"
        right = "----" + diagram[i][4:]
        if left != "--------":
            result[1].append(left)
        if right != "--------":
            result[0].append(right)

    # 빈 레지스터 처리
    if len(result[0]) == 0:
        result[0] = None
    else:
        result[0] = ':'.join(result[0])
    if len(result[1]) == 0:
        result[1] = None
    else:
        result[1] = ':'.join(result[1])
    
    return result


def rotator(diagram, rotateCount):
    if diagram == None:
        return None

    # 회전 작업
    result = []
    diagram = list(map(str, diagram.split(":")))
    for i in range(len(diagram)):
        result.append(diagram[i][2*(4-rotateCount):] + diagram[i][:2*(4-rotateCount)])
    
    return ':'.join(result)


# A와 B를 count칸 만큼 결합
def combine(diagramA, diagramB, combineCount):
    result = []
    for y in range(combineCount):
        temp = ""
        for x in range(0, 8, 2):
            if y >= len(diagramB):
                temp += diagramA[y][x:x+2]
            elif y >= len(diagramA):
                temp += diagramB[y][x:x+2]
            elif diagramA[y][x:x+2] == "--":
                temp += diagramB[y][x:x+2]
            else:
                temp += diagramA[y][x:x+2]
        result.append(temp)

    result2 = []
    for i in result:
        if i != '--------':
            result2.append(i)

    return result2


# A와 B를 최대 몇 칸까지 결합할 수 있는지 확인
def combiner(diagramA, diagramB):
    if diagramA == None or diagramB == None:
        return None
    
    # ":"를 기준으로 나누기
    diagramA = list(map(str, diagramA.split(":")))
    diagramB = list(map(str, diagramB.split(":")))

    # combineCount칸만큼 겹칠 수 있는지 체크
    combineCount = 1
    while combineCount <= len(diagramA):
        rangeA = [x for x in range(len(diagramA)-1, len(diagramA)-combineCount-1, -1)][::-1]
        rangeB = [x for x in range(min(combineCount, len(diagramB)))]

        # 겹치는 모든 칸 체크
        for y in rangeB:
            curA = diagramA[rangeA[y]]
            curB = diagramB[y]
            for x in range(0, 8, 2):
                # 충돌이 일어나는 경우
                if curA[x:x+2] != "--" and curB[x:x+2] != "--":
                    result = diagramA[:len(diagramA)-combineCount+1] + combine(diagramA[len(diagramA)-combineCount+1:], diagramB[:combineCount-1], combineCount-1) + diagramB[combineCount-1:]
                    return ':'.join(result[:4])

        combineCount += 1

    result = diagramA[:len(diagramA)-combineCount+1] + combine(diagramA[len(diagramA)-combineCount+1:], diagramB[:combineCount-1], combineCount-1) + diagramB[combineCount-1:]
    return ':'.join(result[:4])


def coloring(diagram, color):
    if diagram == None:
        return None

    result = []
    diagram = list(map(str, diagram.split(":")))
    for i in range(len(diagram)):
        cur = list(diagram[i])
        for j in range(1, 8, 2):
            if cur[j] != "-":
                cur[j] = color
        result.append(''.join(cur))
    
    return ':'.join(result)


def main():
    N, M = map(int, input().split())
    register = [None for _ in range(101)]
    for i in range(1, N+1):
        register[i] = input().decode().rstrip()
    
    for i in range(M):
        t, i, j, k = map(str, input().decode().rstrip().split())
        if t == '1':
            register[int(j)], register[int(k)] = cutter(register[int(i)])
        elif t == '2':
            register[int(j)] = rotator(register[int(i)], int(k))
        elif t == '3':
            register[int(k)] = combiner(register[int(i)], register[int(j)])
        else:
            register[int(j)] = coloring(register[int(i)], k)

    print(register[100])


main()
