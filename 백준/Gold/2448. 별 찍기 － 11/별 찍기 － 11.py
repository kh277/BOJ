# 백준 2448

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**8


def recur(start, end, isBlank, isRev=False):
    if end - start + 1 == 3:
        if isBlank == False:
            result[start].append('*')
            result[start+1].append('* *')
            result[start+2].append('*****')
        else:
            if isRev == True:
                result[start].append('     ')
                result[start+1].append('   ')
                result[start+2].append(' ')
            else:
                result[start].append(' ')
                result[start+1].append('   ')
                result[start+2].append('     ')
            
        return

    nextGap = (end - start + 1)//2

    if isBlank == False:
        recur(start, start+nextGap-1, False)
        recur(start+nextGap, end, False)
        recur(start+nextGap, end, True, True)
        recur(start+nextGap, end, False)
    else:
        if isRev == True:
            recur(start, start+nextGap-1, True, True)
            recur(start, start+nextGap-1, True)
            recur(start, start+nextGap-1, True, True)
            recur(start+nextGap, end, True, True)
        else:
            recur(start, start+nextGap-1, True)
            recur(start+nextGap, end, True)
            recur(start+nextGap, end, True, True)
            recur(start+nextGap, end, True)

    return


def main():
    global result

    N = int(input())
    result = [[] for _ in range(N)]
    recur(0, N-1, 0)

    for i in range(N):
        print(' '*(N-i-1), end="")
        print(''.join(result[i]), end="")
        print(' '*(N-i-1))


main()
