#include <iostream>

using namespace std;

long long dp[10000001];

int main(){
    int n;
    cin >> n;

    dp[0] = 0;
    dp[1] = 1;
    dp[2] = 2;

    for (int i = 3; i<=n; i++){
        dp[i] = (dp[i - 2] + dp[i - 1]);
        dp[i] %= 15746;
    }
    cout << dp[n];
}