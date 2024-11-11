# [Gold II] Bitcoin - 13218 

[문제 링크](https://www.acmicpc.net/problem/13218) 

### 성능 요약

메모리: 111624 KB, 시간: 476 ms

### 분류

값 / 좌표 압축, 다이나믹 프로그래밍, 그리디 알고리즘, 구현, 수학

### 제출 일자

2024년 11월 11일 15:52:31

### 문제 설명

<p>Bitcoin mining is a very power consuming task. One day, both Ali and Betty wish to start their own mining fields (one field for each of them) in central of Cheras. Hence, Ali and Betty went to Siva, the Mayor of Cheras, to request for locations.</p>

<p>Siva presents Ali and Betty a grid map with the possible locations to set up their mining fields. As Bitcoin mining requires a large amount of power, Siva wants both mining fields to be situated as far as possible from each other to prevent power spikes in the local neighbourhood. Specifically, Siva wants Ali and Betty to maximize the distance between their fields.</p>

<p>Your task is to find the furthest Euclidean (straight line) distance between two possible mining sites given the coordinates of all mining sites. You can assume that the coordinate of a mining site is strictly an integer.</p>

<p>As handling floating points can be tricky (and may cause small precision errors), you are only required to output the square​of the furthest Euclidean distance between the two possible sites for their mining fields.</p>

<p>The square of the Euclidean distance between two points (x<sub>1</sub>, y<sub>1</sub>) and (x<sub>2</sub>, y<sub>2</sub>) is defined as:</p>

<p style="text-align:center">(x<sub>1</sub> - x<sub>2</sub>)<sup>2</sup> + (y<sub>1</sub> - y<sub>2</sub>)<sup>2</sup></p>

### 입력 

 <p>Line 1: A single integer N​, the number of possible mining sites. (2 ≤ N ≤ 1,000,000)</p>

<p>Line 2: A single integer M​ (2 ≤ M ≤ 1,500), the maximum possible absolute value of the mining sites’ coordinates, i.e. -M ≤ x ≤ M and -M ≤ y≤ M where x and y are the coordinates.</p>

<p>Line 3 to (N + 2): Two integers each, coordinates X​<sub>i</sub> ​​and Y<sub>i</sub>​, corresponding to the coordinates of the possible mining sites.</p>

### 출력 

 Empty

