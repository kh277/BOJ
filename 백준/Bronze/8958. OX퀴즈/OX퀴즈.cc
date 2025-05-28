#include <iostream>

int main()
{
    int N = 0;
    std::cin >> N;
    
    int token = 0;
    int sum = 0;
    int *arr = new int[N];
    std::string str;
    for (int i = 0; i < N; i++)
    {
        sum = 0;
        token = 0;
        std::cin >> str;
        for (char s : str)
        {
            if (s == 'O')
            {
                token++;
                sum += token;
            }
            else
                token = 0;
        }
        arr[i] = sum;
    }
    
    for (int j = 0; j < N; j++)
    {
        std::cout << arr[j] << "\n";
    }
    delete arr;
    return 0;
}