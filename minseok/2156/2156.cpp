#include <iostream>
#include <algorithm>

#define Max 100000

using namespace std;

int main(){
    int T;
    int wine[Max] = {0,};
    int dp[Max] = {0,};
    cin >> T;
    for(int i = 1; i<=T ; i++){
        cin >> wine[i];
    }

    dp[0] = wine[0];
    dp[1] = wine[1];
    dp[2] = wine[1] + wine[2];
    for(int i = 3 ; i<=T ; i++){
        dp[i] = max(dp[i-3]+wine[i-1]+wine[i],max(dp[i-2]+wine[i], dp[i-1]));
    }
    cout << dp[T];
}