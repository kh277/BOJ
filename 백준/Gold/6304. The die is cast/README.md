# [Gold V] The die is cast - 6304 

[문제 링크](https://www.acmicpc.net/problem/6304) 

### 성능 요약

메모리: 115276 KB, 시간: 156 ms

### 분류

그래프 이론, 그래프 탐색, 정렬, 너비 우선 탐색, 깊이 우선 탐색, 격자 그래프, 플러드 필

### 제출 일자

2025년 7월 23일 11:08:36

### 문제 설명

<p>InterGames is a high-tech startup company that specializes in developing technology that allows users to play games over the Internet. A market analysis has alerted them to the fact that games of chance are pretty popular among their potential customers. Be it Monopoly, ludo or backgammon, most of these games involve throwing dice at some stage of the game.</p>

<p>Of course, it would be unreasonable if players were allowed to throw their dice and then enter the result into the computer, since cheating would be way to easy. So, instead, InterGames has decided to supply their users with a camera that takes a picture of the thrown dice, analyzes the picture and then transmits the outcome of the throw automatically.</p>

<p>For this they desperately need a program that, given an image containing several dice, determines the numbers of dots on the dice.</p>

<p>We make the following assumptions about the input images. The images contain only three dif- ferent pixel values: for the background, the dice and the dots on the dice. We consider two pixels connected if they share an edge – meeting at a corner is not enough. In the figure, pixels A and B are connected, but B and C are not.</p>

<p style="text-align: center;"><img alt="" src="https://www.acmicpc.net/upload/images2/die.png" style="height:156px; width:155px"></p>

<p>A set s of pixels is connected if for every pair (a,b) of pixel in S, there is a sequence a<sub>1</sub>, a<sub>2</sub>, ..., a<sub>k</sub> in S such that a = a<sub>1</sub> and b = a<sub>k</sub>, and a<sub>i</sub> and a<sub>i+1</sub> are connected for 1 ≤ i < k.</p>

<p>We consider all maximally connected sets consisting solely of non-background pixels to be dice. 'Maximally connected' means that you cannot add any other non-background pixels to the set without making it dis-connected. Likewise we consider every maximal connected set of dot pixels to form a dot.</p>

### 입력 

 <p>The input consists of pictures of several dice throws. Each picture description starts with a line containing two numbers w and h, the width and height of the picture, respectively. These values satisfy 5 ≤ w,h ≤ 50.</p>

<p>The following h lines contain w characters each. The characters can be: "." for a background pixel, "*" for a pixel of a die, and "X" for a pixel of a die's dot.</p>

<p>Dice may have different size and not be entirely square due to optical distortion. The picture will contain at least one die, and the numbers of dots per die is between 1 and 6, inclusive.</p>

<p>The input is terminated by a picture starting with w = h = 0, which should not be processed.</p>

### 출력 

 <p>For each throw of dice, first output its number. Then output the number of dots on the dice in the picture, sorted in increasing order.</p>

<p>Print a blank line after each test case.</p>

