# [Gold III] Hotel booking - 6501 

[문제 링크](https://www.acmicpc.net/problem/6501) 

### 성능 요약

메모리: 214868 KB, 시간: 4140 ms

### 분류

그래프 이론, 그래프 탐색, 너비 우선 탐색, 최단 경로, 데이크스트라, 0-1 너비 우선 탐색

### 제출 일자

2025년 11월 27일 13:26:41

### 문제 설명

<p>A transport company often needs to deliver goods from one city to another city. The transport company has made a special deal with a hotel chain which allows its drivers to stay in the hotels of this chain for free. Drivers are only allowed to drive up to 10 hours a day. The transport company wants to find a route from the starting city to the destination city such that a driver can always spend the night in one of the hotels of the hotel chain, and that he needs to drive at most 10 hours from one hotel to the next hotel (or the destination). Of course, the number of days needed to deliver the goods should also be minimized.</p>

### 입력 

 <p>The input file contains several test cases. Each test case starts with a line containing an integer <em>n</em>, (<em>2 ≤ n ≤ 10000</em>), the number of cities to be considered when planning the route. For simplicity, cities are numbered from 1 to <em>n</em>, where 1 is the starting city, and <em>n</em> is the destination city. The next line contains an integer <em>h</em> followed by the numbers <em>c<sub>1</sub>, c<sub>2</sub>, ..., c<sub>h</sub></em> indicating the numbers of the cities where hotels of the hotel chain are located. You may assume that <em>0 ≤ h ≤ min(n, 100)</em>. The third line of each test case contains an integer <em>m</em> (<em>1 ≤ m ≤ 10<sup>5</sup></em>), the number of roads to be considered for planning the route. The following <em>m</em> lines describe the roads. Each road is described by a line containing 3 integers <em>a, b, t</em> (<em>1 ≤ a, b ≤ n</em> and <em>1 ≤ t ≤ 600</em>), where <em>a, b</em> are the two cities connected by the road, and <em>t</em> is the time in minutes needed by the driver to drive from one end of the road to the other. Input is terminated by <em>n = 0</em>.</p>

### 출력 

 <p>For each test case, print one line containing the minimum number of hotels the transport company has to book for a delivery from city 1 to city <em>n</em>. If it is impossible to find a route such that the driver has to drive at most 10 hours per day, print <em>-1</em> instead.</p>

