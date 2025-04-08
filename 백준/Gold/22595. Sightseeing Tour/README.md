# [Gold III] Sightseeing Tour - 22595 

[문제 링크](https://www.acmicpc.net/problem/22595) 

### 성능 요약

메모리: 109768 KB, 시간: 96 ms

### 분류

애드 혹, 그래프 이론, 그리디 알고리즘

### 제출 일자

2025년 4월 8일 23:21:28

### 문제 설명

<p>KM city has N sightseeing areas. Currently every pair of area is connected by a bidirectional road.</p>

<p>However for some reason, Mr. KM, the mayor of this city, decided to make all of these roads one-way . It costs C<sub>i,j</sub> dollars to renovate the road between area i and area j to a one-way road from area i to area j. Of course, Mr. KM is economic and wants to minimize the total cost of the renovation.</p>

<p>On the other hand, because tourism is the most important industry for KM city, there must exists a tour that goes through all the sightseeing areas, visiting each area exactly once. The first and last area of the path need not to be the same. Can you calculate the minimum total cost required for the renovation, given this situation?</p>

### 입력 

 <p>The first line contains the number of sightseeing area N (1 ≤ N ≤ 100). Next N lines describe the integer matrix C, where the j-th element of the i-th row of the input describes C<sub>i,j</sub> (0 ≤ C<sub>i,j</sub> ≤ 1, 000, 000). For each i, you can assume C<sub>i,i</sub> is always zero.</p>

### 출력 

 <p>Output the minimum cost in a line.</p>

