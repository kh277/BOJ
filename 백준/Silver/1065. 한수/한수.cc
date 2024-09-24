#include <iostream>

bool d(int N);

int main()
{
    int N;
    std::cin >> N;
    
    int count = 0;
    for (int i = 1; i < N+1; i++)
    {
        if (d(i) == true)
            count++;
    }
    
    std::cout << count;
}

bool d(int N)
{
    if (N < 100)
        return true;
    else if (N < 1000)
        if ((N / 100) + (N % 10) == 2 * (N / 10 % 10))
            return true;
        else
            return false;
    else if (N = 1000)
        return false;
}