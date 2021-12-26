#include <iostream>
using namespace std;

int main(void)
{
    int n, num;
    int min = 1000001, max = -1000001;
    cin >> n;

    for (int i = 1; i <= n; i++)
    {
        cin >> num;
        if (num > max)
            max = num;
        if (num < min)
            min = num;
    }
    printf("%d %d", min, max);

    return 0;
}