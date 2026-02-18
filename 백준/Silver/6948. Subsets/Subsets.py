# 백준 6948

import io, os

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, dic):
    result = dict()
    for key in sorted(dic.keys()):
        visited = set()
        subset = set()
        stack = [key]
        visited.add(key)

        # 각 키별로 DFS 탐색
        while stack:
            cur = stack.pop()

            # 소문자일 경우
            if 97 <= ord(cur) <= 122:
                subset.add(cur)
            # 대문자일 경우
            else:
                visited.add(cur)
                for i in dic[cur]:
                    if i not in visited:
                        stack.append(i)
        result[key] = subset

    return result


def main():
    N = int(input())
    dic = dict()
    for _ in range(N):
        s, _, e = input().decode().split()
        if s in dic:
            dic[s].append(e)
        else:
            dic[s] = [e]
        if 65 <= ord(e) <= 90:
            if e not in dic:
                dic[e] = []

    # 출력 포매팅
    res = solve(N, dic)
    for k in sorted(res.keys()):
        formatted_elements = ",".join(sorted(res[k]))
        print(f"{k} = {{{formatted_elements}}}")


main()
