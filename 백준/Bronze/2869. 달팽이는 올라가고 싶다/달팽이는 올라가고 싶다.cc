#include <iostream>

int main()
{
    int A = 0;     // 올라가는 미터
    int B = 0;     // 내려오는 미터
    int V = 0;     // 전체 미터
    int count = 1;     // 횟수
    std::cin >> A >> B >> V;
    
    if (A == V)
    {
        std::cout << count;
        return 0;
    }
    
    if (((V - A) % (A - B)) == 0)
        count += (V - A) / (A - B);
    else
        count += (V - A) / (A - B) + 1;
    
    std::cout << count;
    return 0;
}