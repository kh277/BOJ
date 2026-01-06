# [Gold III] The Climbing Wall - 14781 

[문제 링크](https://www.acmicpc.net/problem/14781) 

### 성능 요약

메모리: 120036 KB, 시간: 184 ms

### 분류

0-1 너비 우선 탐색, 너비 우선 탐색, 자료 구조, 데이크스트라, 기하학, 그래프 이론, 그래프 탐색, 정렬, 트리를 사용한 집합과 맵, 최단 경로, 집합과 맵

### 제출 일자

2026년 1월 6일 14:11:11

### 문제 설명

<p>One of the most popular attractions at the county fair is the climbing wall. Bessie wants to plan her trip up the wall in advance and needs your help.</p>

<p>The wall is 30,000 millimeters wide and H (1001 <= H <= 30,000) millimeters high and has F (1 <= F <= 10,000) hoof-holds at unique X,Y coordinates expressed in millimeters. 0,0 is at the ground level on the left side of the wall. Hoof-holds are separated by at least 300 millimeters since no cow can maneuver them if they are spaced too close! Bessie knows there is at least one way up.</p>

<p>Bessie, through techniques only she knows, uses successive single hoof-holds to climb the wall. She can only move from one hoof-hold to another if they are no more than one meter apart. She can, of course, move up, down, right, left or some combination of these in each move. Similarly, once she gets to a hoof-hold that is at least H-1000 millimeters above the ground, she can nimbly climb from there onto the platform atop the wall. Bessie can start at any X location that has a Y location <= 1000 millimeters.</p>

<p>Given the height of the wall and the locations of the hoof-holds, determine the smallest number of hoof-holds Bessie should use to reach the top.</p>

### 입력 

 <ul>
	<li>Line 1: Two space-separated integers, H and F.</li>
	<li>Lines 2..F+1: Each line contains two space-separated integers (respectively X and Y) that describe a hoof-hold. X is the distance from the left edge of the climbing wall; Y is the distance from the ground.</li>
</ul>

### 출력 

 <ul>
	<li>Line 1: A single integer that is the smallest number of hoof-holds Bessie must use to reach the top of the climbing wall.</li>
</ul>

