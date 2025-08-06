# [Gold IV] Balls - 18735 

[문제 링크](https://www.acmicpc.net/problem/18735) 

### 성능 요약

메모리: 129328 KB, 시간: 140 ms

### 분류

애드 혹

### 제출 일자

2025년 8월 6일 11:10:38

### 문제 설명

<p>Zenyk placed n balls in a row on a table, and the i-th ball is colored in color c<sub>i</sub>. Now Marichka is going to play with Zenyk’s balls.</p>

<p>In a single turn, she can pick a sequence of consecutive balls which has a dominant color. After that, all selected balls that are colored in a different color than the dominant will be removed.</p>

<p>Marichka wants to make some number of turns (possibly zero) after which all remaining balls will be colored in the same color. Find out how many different colors could be left at the end.</p>

<p>Color is considered dominant if more than half of the selected balls are colored in it.</p>

### 입력 

 <p>The first line contains a single integer n (1 ≤ n ≤ 10<sup>5</sup>) — the number of balls. The second line contains a list of n space-separated integers c<sub>i</sub> (1 ≤ c<sub>i</sub> ≤ 10<sup>9</sup>) — the initial colors of the balls in the order they are placed on the table.</p>

### 출력 

 <p>In the only line print a single integer — the answer to the problem.</p>

