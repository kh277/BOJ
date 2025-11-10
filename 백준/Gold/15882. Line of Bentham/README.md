# [Gold I] Line of Bentham - 15882 

[문제 링크](https://www.acmicpc.net/problem/15882) 

### 성능 요약

메모리: 251516 KB, 시간: 976 ms

### 분류

비트마스킹, 다이나믹 프로그래밍, 비트필드를 이용한 다이나믹 프로그래밍

### 제출 일자

2025년 11월 10일 16:19:26

### 문제 설명

<p>공리주의 국가의 한 장소에 N명의 사람들이 앞을 보고 일렬로 줄을 설 예정이다. 맨 앞 사람을 1번이라고 하고, 쭉 숫자를 붙여 맨 뒤에 서 있는 사람을 N번이라고 하자.</p>

<p>이 사람들은 좋아하는 사람과 싫어하는 사람이 명확하다. 한 사람은 앞을 봤을 때 자기 앞의 3명까지 분간할 수 있는데, 자기 앞에 보이는 사람 중에 싫어하는 사람이 있으면 싫어하는 만큼 기분이 나빠지고, 좋아하는 사람이 있으면 좋아하는 만큼 기분이 좋아진다.</p>

<p>국가에서는 이를 수치화시켜서 행복 지수를 정의했다. i번 사람이 j번 사람을 좋아하는 정도 p<sub>i,j</sub> 를 -10에서 10 사이의 정수로 측정한 뒤, i번 사람의 행복 지수 q<sub>i</sub>를 p<sub>i,i−3</sub> + p<sub>i,i−2</sub> + p<sub>i,i−1</sub> 로 정의했다. (단, j ≤ 0인 p<sub>i,j</sub>는 j번 사람이 실존하지 않기 때문에 0으로 정의한다.) 그리고 N명의 행복 지수를 모두 더한 것인 <mjx-container class="MathJax" jax="CHTML" style="font-size: 101.8%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D444 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c3D"></mjx-c></mjx-mo><mjx-munderover space="4" limits="false"><mjx-mo class="mjx-sop"><mjx-c class="mjx-c2211 TEX-S1"></mjx-c></mjx-mo><mjx-script style="vertical-align: -0.285em; margin-left: 0px;"><mjx-texatom size="s" texclass="ORD"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-texatom><mjx-spacer style="margin-top: 0.291em;"></mjx-spacer><mjx-texatom size="s" texclass="ORD"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c3D"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-texatom></mjx-script></mjx-munderover><mjx-texatom space="2" texclass="ORD"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45E TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.014em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msub></mjx-texatom></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mo>=</mo><munderover><mo data-mjx-texclass="OP">∑</mo><mrow data-mjx-texclass="ORD"><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mrow data-mjx-texclass="ORD"><mi>N</mi></mrow></munderover><mrow data-mjx-texclass="ORD"><msub><mi>q</mi><mi>i</mi></msub></mrow></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">\(Q =\sum_{i=1}^{N}{q_i}\)</span></mjx-container> 를 종합 행복지수로 정의하고, 이를 최대화 시키는 것을 원한다.</p>

<p>그래서 국가 검열관 정현식은 줄에서 사람들을 임의로 몇 명 제외하고, 그 자리에 대신 누구와도 면식이 없는 정부 파견 요원을 넣는 임무를 받게 되었다.</p>

<p>특정 자리에 요원을 넣게 되면, 요원은 좋아하거나 싫어하는 사람이 없기 때문에 요원의 행복 지수는 0이며, 요원의 뒤에 있는 사람들은 해당 요원을 좋아하지도 싫어하지도 않을 것이다. 투입할 수 있는 요원은 수없이 많기 때문에, 줄의 몇 명을 요원으로 대체해도 문제는 없다.</p>

<p>검열관 정현식을 도와 N명의 사람들로부터 얻을 수 있는 종합 행복 지수의 최댓값을 구해보자.</p>

### 입력 

 <p>첫 번째 줄에 사람의 수 N(3 ≤ N ≤ 1, 000, 000)이 들어온다.</p>

<p>두 번째 줄부터는 한 줄 씩 1부터 N 사이의 i번 사람에 대한 정보가 들어온다.</p>

<p>i + 1(1 ≤ i ≤ N)번째 줄에는 정수 3개 p<sub>i,i−3</sub>, p<sub>i,i−2</sub>, p<sub>i,i−1</sub> 가 입력된다.</p>

<p>j ≤ 0인 p<sub>i,j</sub>를 입력받는 경우, j번 사람은 실존하지 않는 사람이기 때문에 무조건 p<sub>i,j</sub> = 0이다. 그 외의 경우, p<sub>i,j</sub>는 -10 이상 10 이하의 정수로 주어진다.</p>

### 출력 

 <p>N명 중 일부를 요원으로 바꿔서 얻을 수 있는 종합 행복 수치 중 최댓값을 출력한다.</p>

