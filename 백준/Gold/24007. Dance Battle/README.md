# [Gold IV] Dance Battle - 24007 

[문제 링크](https://www.acmicpc.net/problem/24007) 

### 성능 요약

메모리: 110940 KB, 시간: 100 ms

### 분류

다이나믹 프로그래밍, 그리디 알고리즘, 정렬

### 제출 일자

2025년 6월 5일 13:31:31

### 문제 설명

<p>Your team is about to prove itself in a dance battle! Initially, your team has <b>E</b> points of energy, and zero points of honor. There are <b>N</b> rival teams who you must face; the i-th of these teams is the i-th in a lineup, and has a dancing skill of <b>S<sub>i</sub></b>.</p>

<p>In each round of battle, you will face the next rival team in the lineup, and you can take one of the following actions:</p>

<ol>
	<li><i>Dance</i>: Your team loses energy equal to the dancing skill of the rival team, and that team does not return to the lineup. You gain one point of honor. You cannot take this action if it would make your energy drop to 0 or less.</li>
	<li><i>Delay</i>: You make excuses ("our shoes aren't tied!") and the rival team returns to the back of the lineup. Your energy and honor do not change.</li>
	<li><i>Truce</i>: You declare a truce with the rival team, and that team does not return to the lineup. Your energy and honor do not change.</li>
	<li><i>Recruit</i>: You recruit the rival team onto your team, and that team does not return to the lineup. Your team gains energy equal to the dancing skill of the rival team, but you lose one point of honor. You cannot take this action if it would make your honor drop below 0.</li>
</ol>

<p>The battle is over when there are no more rival teams in the lineup. If you make optimal decisions, what is the maximum amount of honor you can have when the battle is over?</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <b>T</b>. <b>T</b> test cases follow; each consists of two lines. The first line consists of two integers <b>E</b> and <b>N</b>: your team's energy, and the number of rival teams. The second line consists of <b>N</b> integers <b>S<sub>i</sub></b>; the i-th of these represents the dancing skill of the rival team that is i-th in line at the start of the battle.</p>

### 출력 

 <p>For each test case, output one line containing <code>Case #x: y</code>, where <code>x</code> is the test case number (starting from 1) and <code>y</code> is the maximum amount of honor you can have when the battle is over.</p>

