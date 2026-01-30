# [Gold III] Taxi! - 7804 

[문제 링크](https://www.acmicpc.net/problem/7804) 

### 성능 요약

메모리: 110932 KB, 시간: 100 ms

### 분류

데이크스트라, 다이나믹 프로그래밍, 그래프 이론, 최단 경로

### 제출 일자

2026년 1월 31일 01:27:26

### 문제 설명

<ul>
	<li>Taxi Driver    :  "Where to go, sir?"</li>
	<li>Passenger    :  "Kemanggisan, Binus Campus, please."</li>
	<li>Taxi Driver    :  "Okay, and which way to go?"</li>
	<li>Passenger    :  "Just take the fastest one."</li>
</ul>

<p>This kind of conversation usually happens when we take a taxi. Many people think that the fastest way would mean the cheapest one as well. But it’s not always true! Sometimes the fastest way could be more expensive than the slower one and vice versa, some factors are: toll fee, longer road without traffic jam, etc.</p>

<p>We will model this kind of situation on this problem. The city has n intersections and m bidirectional roads connecting pairs of intersections. Each road will cost you a certain time and money (taxi fare). Write a program to find the minimum time to take you to your destination however the travel expenses must not exceed your money.</p>

### 입력 

 <p>The first line of each case contains two integers, n (1 <= n <= 100) intersections and m roads. The intersections are numbered from 0 to n-1. The next m lines will each contains four integers: u, v, t, and c (1 <= t,c <= 100), means that there is a road from intersection u to intersection v and vice versa which will cost you t minute(s) and c Rupiah(s). The last line of each case will contains three integers: s, d, and r (1 <= r <= 100), means that you want to go to d (your destination point) from s (your starting point) while you only have r Rupiah(s).</p>

<p> </p>

### 출력 

 <p>For each case, output in a single line the minimum time to reach your destination while the total cost doesn’t exceed your money.</p>

<p> </p>

