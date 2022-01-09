#include <iostream>
using namespace std;

int CountZero = 0;
int CountOne = 0;

int fibo(int n){
    if (n=0){
        CountZero++;
        return 0;
    }
    else if(n ==1){
        CountOne++;
        return 1;
    }
    else{
        return fibo(n-1)+fibo(n-2);
    }
}

int main(){
    int T;
    cin >> T;
    int n[T];

    for (int i=0;i<T;i++){
        cin >> n[i];
    }

    for (int i=0;i<T;i++){
        fibo(n[i]);
    }

    cout <<CountZero<<" "<<CountOne<<endl;

    CountOne=0;
    CountZero=0;
}