# [Gold IV] River Crossing - 6176 

[문제 링크](https://www.acmicpc.net/problem/6176) 

### 성능 요약

메모리: 111092 KB, 시간: 156 ms

### 분류

다이나믹 프로그래밍

### 제출 일자

2025년 3월 9일 21:01:30

### 문제 설명

<p>Farmer John is herding his N cows (1 <= N <= 2,500) across the expanses of his farm when he finds himself blocked by a river. A single raft is available for transportation.</p>

<p>FJ knows that he must ride on the raft for all crossings and that that adding cows to the raft makes it traverse the river more slowly.</p>

<p>When FJ is on the raft alone, it can cross the river in M minutes (1 <= M <= 1000).  When the i cows are added, it takes M_i minutes (1 <= M_i <= 1000) longer to cross the river than with i-1 cows (i.e., total M+M_1 minutes with one cow, M+M_1+M_2 with two, etc.). Determine the minimum time it takes for Farmer John to get all of the cows across the river (including time returning to get more cows).</p>

### 입력 

 <ul>
	<li>Line 1: Two space-separated integers: N and M</li>
	<li>Lines 2..N+1: Line i+1 contains a single integer: M_i</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Line 1: The minimum time it takes for Farmer John to get all of the cows across the river.</li>
</ul>

