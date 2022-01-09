#include <iostream>

using namespace std;

class fibo{
    private:
    int Count_0 = 0;
    int Count_1 = 0;
    int N;

    public:
    int fibonacci(int);
    void add0();
    void add1();
    void result();
};

void fibo::add0(){
     Count_0++;
}

void fibo::add1(){
    Count_1++;
}

int fibo::fibonacci(int n){
    if(n == 0){
        fibo::add0();
        return 0;
    }

    else if(n == 1){
        fibo::add1();
        return 1;
    }

    else{
        return (fibonacci(n-1) + fibonacci(n-2));
    }
}

void fibo::result(){
    cout << fibo::Count_0 << " " << fibo::Count_1 << endl;
}

int main(){
    int T = 0;
    cin >> T;
    
    for (int i = 0 ; i < T ; i++){
        int N;
        cin >> N;
        fibo fibo;
        fibo.fibonacci(N);
        fibo.result();
    }
}