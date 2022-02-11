#include<iostream>
using namespace std;

int main(){
    int T,N;
    long int provan[101] = {0};
    cin >>T;
    
    for(int i = 1 ; i < 4 ; i++) provan[i] = 1;
    for(int i = 4 ; i < 101 ; i++){
            provan[i] = provan[i-2] + provan[i-3];
        }
 
    for(int t = 0; t < T; t++)
    {
        cin >> N;
        cout << provan[N] <<endl;
    }
}