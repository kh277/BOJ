# 백준 33576

'''
벽은 바깥쪽부터 안쪽으로 부서지게 되므로,
투 포인터를 양쪽 끝부터 시작해서 안쪽으로 이동하며 벽이 부서진 위치를 가리키도록 처리하면 된다.
벽의 합은 누적합을 이용하면 된다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


# 두 구간은 (1, leftP], [rightP, N) 벽이 부서진 위치를 나타내며, 학생의 위치 pos에서 결과 반환
def query(N, accSum, leftP, rightP, pos):
    if pos <= leftP or rightP <= pos:
        return [leftP, rightP, 0]

    leftSum = accSum[pos] - accSum[leftP]
    rightSum = accSum[rightP] - accSum[pos]
    result = 0

    # 왼쪽 벽의 누적합이 더 작은 경우
    if leftSum < rightSum:
        leftP = pos
        result = leftSum

    # 오른쪽 벽의 누적합이 더 작은 경우
    elif leftSum > rightSum:
        rightP = pos
        result = rightSum

    # 양쪽이 동일한 경우
    else:
        leftDistance = pos - 1
        rightDistance = N - pos
        # 왼쪽까지 거리가 더 작은 경우
        if leftDistance < rightDistance:
            leftP = pos
        # 오른쪽까지 거리가 더 작은 경우
        elif leftDistance > rightDistance:
            rightP = pos
        # 거리가 같은 경우
        else:
            leftP = pos
        result = leftSum

    return [leftP, rightP, result]


def main():
    N, M, Q = map(int, input().split())

    wall = [0 for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        wall[a] = b
    
    accSum = [0]        # 0번 누적합은 미사용
    for i in range(1, N+1):
        accSum.append(accSum[i-1] + wall[i])

    leftP = 0
    rightP = N
    for _ in range(Q):
        pos = int(input())
        leftP, rightP, result = query(N, accSum, leftP, rightP, pos)
        print(result)


main()