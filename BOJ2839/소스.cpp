#include <iostream>

int main()
{
    int N;     // 여기서 N은 3 이상
    std::cin >> N;
    int count = 0;

    // 5로 나눠서 1이 남는 경우 -> 나머지를 6+a로 만들기
    // N이 6+a를 만족하지 않는 경우는 N = 1일 경우일 때 뿐이므로 예외상황 X    
    if ((N % 5) == 1)
        count = N / 5 + 1;

    // 5로 나눠서 2이 남는 경우 -> 나머지를 12+a로 만들기
    // N이 12+a를 만족하지 않는 경우는 N = 2, 7인 경우
    else if ((N % 5) == 2)
    {
        if (N != 7)
            count = N / 5 + 2;
        else
            count = -1;
    }

    // 5로 나눠서 3이 남는 경우 -> 나머지를 3+a로 만들기
    // N이 3+a를 만족하지 않는 경우는 없음
    else if ((N % 5) == 3)
        count = N / 5 + 1;

    // 5로 나눠서 4가 남는 경우 -> 나머지를 9+a로 만들기
    // N이 9+a를 만족하지 않는 경우는 N = 4인 경우   
    else if ((N % 5) == 4)
    {
        if (N != 4)
            count = N / 5 + 2;
        else
            count = -1;
    }

    // 5로 나눠서 나눠떨어지는 경우 
    else
        count = N / 5;

    std::cout << count;
    return 0;
}