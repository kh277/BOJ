# [Gold IV] Circular Caramel Cookie - 26176 

[문제 링크](https://www.acmicpc.net/problem/26176) 

### 성능 요약

메모리: 110960 KB, 시간: 200 ms

### 분류

수학, 이분 탐색

### 제출 일자

2026년 1월 6일 13:50:05

### 문제 설명

<p>Stroopwafels -- two crispy round waffles with a grid-like pattern on top, separated by a thin layer of gooey and delicious caramel -- are simply the most amazing Dutch treat ever. Everybody loves them and your factory is known for making the best and the biggest stroopwafels in town\dots{} At least, until now.</p>

<p>This year, your archrival Rob had the audacity to open up another factory for stroopwafels and they have already announced that their stroopwafels will be even bigger than yours. Although the exact size of the new stroopwafels is a well-kept secret, your industrial spy managed to find out that the grid-like pattern of the stroopwafel consists of at most $s$ whole squares. You know for a fact that the area of each square is $1 \text{cm}^2$ and that the centre point of the stroopwafel always contains the common corner of the four adjacent squares in the centre (i.e., the squares are aligned to a Cartesian grid), as shown in Figure C.1.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/c48ec0b9-694e-414a-af4e-fdfbc4b87abc/-/preview/" style="width: 160px; height: 162px;"></p>

<p style="text-align: center;">Figure C.1: Illustration of Sample Input 2, with the blue-enclosed region depicting the $60$ whole squares that the cookie contains.</p>

<p>Needless to say, there is no way that you will let Rob outdo you and you plan on releasing a new edition of bigger stroopwafels. Since the production of bigger stroopwafels is more expensive, you naturally want to make them as small as possible. Thus, you are interested in the minimum radius of a stroopwafel with strictly more than $s$ squares.</p>

### 입력 

 <p>The input consists of:</p>

<ul>
	<li>One line with an integer $s$ ($1\leq s\leq 10^9$), the number of whole squares Rob's stroopwafel has at most.</li>
</ul>

### 출력 

 <p>Output the minimum radius in centimetres of a stroopwafel with strictly more than $s$ whole squares. Your answer should have an absolute or relative error of at most $10^{-6}$.</p>

