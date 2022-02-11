#include <iostream>
#include <algorithm>
    
using namespace std;

int main(){
    int T;
    int House[1001][3] = {0,};
    
    cin >> T;
    for(int i = 0 ; i <= T ; i++){
        cin >> House[i][0] >> House[i][1] >> House[i][2];

        House[i][0] += min(House[i-1][1],House[i-1][2]);
        House[i][1] += min(House[i-1][0],House[i-1][2]);
        House[i][2] += min(House[i-1][0],House[i-1][1]);
    }
    int result = min(House[T][0], min(House[T][1],House[T][2]));
    cout << result;
}