# [Gold V] Space Emergency (Large) - 12494 

[문제 링크](https://www.acmicpc.net/problem/12494) 

### 성능 요약

메모리: 226164 KB, 시간: 4096 ms

### 분류

자료 구조, 그리디 알고리즘, 우선순위 큐

### 제출 일자

2024년 11월 7일 15:10:19

### 문제 설명

<p>There's an emergency—in space! You need to send your fleet's flagship as quickly as possible from star 0 to star <strong>N</strong>, traveling through the other stars in increasing numerical order along the way (0→1→...→<strong>N</strong>). Your flagship normally travels at a speed of 0.5 parsecs per hour.</p>

<p>In addition to sending your flagship, you can order your engineers to build up to <strong>L</strong> speed boosters at different stars. Building a speed booster takes <strong>t</strong> hours, and all <strong>L</strong> speed boosters can be built in parallel. While your flagship travels from a star with a completed speed booster to the next star, its speed is 1 parsec per hour.</p>

<p>If a speed booster is completed at a star while your flagship is traveling from that star to the next one, your flagship will start moving faster as soon as the speed booster is completed.</p>

<p>How many hours does it take your flagship to get to star <strong>N</strong> if you build speed boosters to make it arrive as soon as possible?</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>.  <strong>T</strong> lines follow. Each contains integers, <strong>L</strong>, <strong>t</strong>, <strong>N</strong> and <strong>C</strong>, followed by <strong>C</strong> integers <strong>a<sub>i</sub></strong>, all separated by spaces.  <strong>a<sub>i</sub></strong> is the number of parsecs between star <strong>k*C</strong>+i and star <strong>k*C</strong>+i+1, for all integer values of <strong>k</strong>.</p>

<p>For example, with <strong>N</strong>=8, <strong>C</strong>=3, <strong>a<sub>0</sub></strong>=3, <strong>a<sub>1</sub></strong>=5 and <strong>a<sub>2</sub></strong>=4, the distances between stars are [3, 5, 4, 3, 5, 4, 3, 5].</p>

<h3>Limits</h3>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 100.</li>
	<li>1 ≤ <strong>C</strong> ≤ 1000.</li>
	<li><strong>C</strong> ≤ <strong>N</strong>.</li>
	<li>1 ≤ <strong>a<sub>i</sub></strong> ≤ 10<sup>4</sup>.</li>
	<li>0 ≤ <strong>t</strong> ≤ 10<sup>11</sup>.</li>
	<li><strong>t</strong> is even.</li>
	<li>1 ≤ <strong>N</strong> ≤ 10<sup>6</sup>.</li>
	<li>0 ≤ <strong>L</strong> ≤ N.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is a single integer: the number of hours it takes to reach star <strong>N</strong>. The answer is guaranteed to always be an integer.</p>

