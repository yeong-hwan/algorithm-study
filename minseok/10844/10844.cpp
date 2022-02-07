#include <iostream>
#define bil 1000000000
using namespace std;

int stair[101][10] = {0,};

int main(){
    int N ;
    cin >> N;

    for(int i = 1 ; i < 10 ; i++){
        stair[1][i] = 1;
    }

    for(int i = 2 ; i <= N ; i++)
    {
        for(int j = 0 ; j < 10 ; j++){
            if(j==0)
                stair[i][0] = stair[i-1][j+1];
            else if(j==9)
                stair[i][9] = stair[i-1][j-1];
            else
                stair[i][j] = stair[i-1][j-1] + stair[i-1][j+1];

            stair[i][j] %= bil;
        }
    }
    
    int sum = 0;
    for (int i = 0 ; i < 10; i++)
        sum = (sum+stair[N][i])%bil;

    cout << sum <<endl;
    return 0;
}