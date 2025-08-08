# [Silver II] Even More Dice - 9294 

[문제 링크](https://www.acmicpc.net/problem/9294) 

### 성능 요약

메모리: 111476 KB, 시간: 144 ms

### 분류

백트래킹, 재귀

### 제출 일자

2025년 8월 8일 09:54:34

### 문제 설명

<p>At Carlisle’s Casino there’s a new dice game that everyone is talking about. Given n dice, each with m sides, the player has to roll the sum randomly chosen by the dealer. For each number given by the dealer, compute the possible rolls that would result in that sum.</p>

### 입력 

 <p>The first line of input is a single integer, c, representing the number of test cases. the next line contains three space-separated integers, representing the n, the number of dice, and m, the number of sides that each die has, and finally s, the sum that must be rolled.</p>

### 출력 

 <p>For each case, output the line “Case x:” where x is the case number, on a single line. Then list each of the possible dice combinations that result in that sum, one on each line. Each dice value should be comma-separated and enclosed by parentheses. All dice must be used in each set. Each ordered set should be least to greatest when reading from left to right, and one permutation of each combination should be shown. For example, (1,2,3) is correct where as (2,3,1) (2,1,3) (3,1,2) (3,2,1) (1,3,2) are incorrect.</p>

