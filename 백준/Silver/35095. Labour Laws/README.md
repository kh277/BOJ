# [Silver III] Labour Laws - 35095 

[문제 링크](https://www.acmicpc.net/problem/35095) 

### 성능 요약

메모리: 108608 KB, 시간: 84 ms

### 분류

애드 혹, 많은 조건 분기

### 제출 일자

2026년 1월 11일 00:14:47

### 문제 설명

<p>The "Arbeitszeitgesetz" (ArbZG) regulates the work and break times of employees in Germany. According to this law, if an employee works more than 6 hours on a given day, the employee <strong>must</strong> take a break of at least half an hour during their shift. If they work for more than 9 hours, their break must be at least 45 minutes. Additionally, working for more than 10 hours on a day is strictly forbidden.</p>

<p>Alexander works at his company's HR department. As the working hours at his company are very flexible, the employees are allowed to work as many hours or as few as they want (within the legal constraints of course). The monthly salary for each employee thus depends on the time spent working. Therefore, one of Alexander's monthly tasks is to collect the times each employee has worked on any given day, so that he can calculate and pay out the employees salaries every month.</p>

<p>Unfortunately, today one of his colleagues forgot to record her lunch break and cannot remember how much time she spent on her break. As Alexander does not want to put his colleague at a disadvantage, he wants to use the legally required minimum break time for his calculations.</p>

<p>While calculating the total time his coworker spent at work is easy, correctly calculating the legally required minimum break time can be tricky. Can you help Alexander determine the minimum time his coworker must have spent at lunch today? Note that the time spent at work is the time spent working plus the time spent in break.</p>

### 입력 

 <p>The input consists of:</p>

<ul>
<li>One line with an integer <mjx-container class="MathJax" jax="CHTML" style="font-size: 101.8%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D461 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$t$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 101.8%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D461 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c34"></mjx-c><mjx-c class="mjx-c34"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>≤</mo><mi>t</mi><mo>≤</mo><mn>1440</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$0\leq t\leq 1440$</span></mjx-container>), the number of minutes spent at work today.</li>
</ul>

### 출력 

 <p>Output a single non-negative integer, the minimum number of minutes spent in break to make the work time legal.</p>

