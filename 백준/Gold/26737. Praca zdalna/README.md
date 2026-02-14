# [Gold V] Praca zdalna - 26737 

[문제 링크](https://www.acmicpc.net/problem/26737) 

### 성능 요약

메모리: 125228 KB, 시간: 140 ms

### 분류

수학, 정렬

### 제출 일자

2026년 2월 15일 00:57:53

### 문제 설명

<p>Bajtazar z racji pandemii pracuje zdalnie. Ponieważ wszyscy jego współpracownicy pracują ze swoich rodzinnych krajów z różnymi strefami czasowymi, coraz trudniej jest ustalić wspólny termin comiesięcznego spotkania. Spotkanie to powinno rozpocząć się o pełnej godzinie i trwać dokładnie godzinę.</p>

<p>Każdy pracownik ma kalendarz, w którym jest zaznaczony przedział czasu, w którym może wziąć udział w spotkaniu: i-ty pracownik zaczyna pracę o godzinie A<sub>i</sub>, a kończy pracę po godzinie B<sub>i</sub>. Oznacza to, że pracownik i może wziąć udział w spotkaniu o dowolnej godzinie od A<sub>i</sub> do B<sub>i</sub> (włącznie).</p>

<p>Każdy z pracowników jest także gotowy zostać po godzinach albo zacząć wcześniej niż to co zadeklarował. Nikt nie zrobi jednak tego za darmo: za każdą godzinę spędzoną dłużej w pracy należy zapłacić pracownikowi bajtodolara.</p>

<p>Wyznacz termin, w którym można zorganizować spotkanie tak, żeby każdy z pracowników (być może za dodatkową opłatą) mógł w nim uczestniczyć, a opłata za nadgodziny była jak najmniejsza.</p>

### 입력 

 <p>W pierwszym wierszu wejścia znajduje się jedna liczba naturalna N (1 ≤ N ≤ 100 000) oznaczające liczbę pracowników. Następnie w N wierszach znajdują się dwie liczby całkowite A<sub>i</sub> oraz B<sub>i</sub> (0 ≤ A<sub>i</sub> ≤ B<sub>i</sub> ≤ 10<sup>9</sup>) oznaczające okienko pracy i-tego pracownika, przy czym A<sub>i</sub> to godzina rozpoczęcia pracy, natomiast B<sub>i</sub> to godzina po której opuści on pracę.</p>

### 출력 

 <p>Na standardowe wyjście należy wypisać dwie liczby w pojedynczym wierszu – liczbę T oznaczającą moment rozpoczęcia spotkania oraz liczbę K oznaczającą sumaryczną opłatę za nadgodziny.</p>

<p>Jeśli istnieje wiele możliwych rozwiązań, Twój program może wypisać dowolne z nich.</p>

