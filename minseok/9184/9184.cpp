#include<iostream>

using namespace std;

int a,b,c;
int dp[21][21][21];

int w(int a,int b,int c){
    if(a<=0 or b<=0 or c<=0)
        return 1;
    else if(a>20 or b>20 or c>20)
        return w(20,20,20);

    else if(a<b and b<c){
        if (dp[a][b][c] != 0) 
            return dp[a][b][c];

		else 
            return dp[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c);
    }
    else{
        if (dp[a][b][c] != 0)
            return dp[a][b][c];
        
        else
            return dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1);        
    }

}

int main(){
    while(1){
        cin >> a >> b >> c;
        if(a == -1 and b == -1 and c == -1) break;

        cout << "w(" << a << ", " << b << ", " << c <<") = " << w(a,b,c) << endl;

    }    
}