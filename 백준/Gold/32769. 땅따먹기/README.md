# [Gold IV] 땅따먹기 - 32769 

[문제 링크](https://www.acmicpc.net/problem/32769) 

### 성능 요약

메모리: 114640 KB, 시간: 148 ms

### 분류

백트래킹, 너비 우선 탐색, 그래프 이론, 그래프 탐색

### 제출 일자

2024년 11월 26일 21:39:52

### 문제 설명

<p>체육 시간에 세종이, 영진이, 은찬이는 땅따먹기 게임을 하고 있었다. 이 게임은 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-cD7"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="3"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi><mo>×</mo><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N \times M$</span></mjx-container> 크기의 격자로 이루어진 구역을 여러 영역으로 나누어 가지는 게임이다.</p>

<p>게임을 하던 중, 게임이 끝나기 전에 종이 치는 바람에 셋은 하고 있던 게임 상황을 기록해 놓고 다시 돌아오기로 했다. 기록은 다음과 같은 규칙으로 남겨진다.</p>

<ul>
	<li>각 칸에는 그 칸이 속한 영역을 나타내는 정수가 적혀 있다. 같은 정수가 적혀 있는 칸은 연결되어 있지 않더라도 같은 영역이다.</li>
	<li>하나의 영역은 모두 한 사람의 소유이며 이웃한 두 영역은 서로 다른 사람의 소유여야 한다. 단, 1번 영역과 2번 영역이 이웃한다는 것은 영역 1의 칸 중 상하좌우에 영역 2의 칸이 있는 것이 존재한다는 것을 의미한다.</li>
</ul>

<p>게임을 마저 진행하러 돌아온 세 사람은 게임의 기록을 확인하고는 원래의 게임 상황과 다른 것 같다는 위화감을 느꼈다. 자리를 비운 사이에 스파이가 침입해서 기록을 조작했다고 생각한 그들은 게임의 기록이 올바른지 확인하고자 한다. 게임 기록을 바탕으로 규칙에 맞게 모든 영역을 세 사람 중 한 명이 소유할 수 있다면 이는 올바른 게임 기록이다. 세 사람은 게임 기록이 올바르지 않다면 스파이가 침입한 것이 확실하니 게임을 처음부터 다시 시작하고, 게임 기록이 올바르다면 그 기록에 따라 마저 게임을 진행하기로 했다.</p>

<p>하지만 이들은 게임을 미루면서 기록이 올바른지 확인할 인내심이 없다. 그러니, 여러분이 기록이 올바른지 확인해 주자.</p>

### 입력 

 <p>첫째 줄에 높이 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>, 너비 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M$</span></mjx-container>이 공백을 구분으로 주어진다. (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="2"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>≤</mo><mi>N</mi><mo>,</mo><mi>M</mi><mo>≤</mo><mn>200</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$2 \le N, M \le 200$</span></mjx-container>)</p>

<p>둘째 줄부터 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>개의 줄에 걸쳐 게임 기록이 주어진다. 단, 각 칸에 적혀 있는 수는 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$20$</span></mjx-container> 이하의 양의 정수다.</p>

### 출력 

 <p>첫째 줄에 스파이가 침입한 것이 확실한 경우 <span style="color:#e74c3c;"><code>Wrong</code></span>을 출력하고, 확실하지 않은 경우 <code><span style="color:#e74c3c;">Not Sure</span></code>를 출력한다.</p>

