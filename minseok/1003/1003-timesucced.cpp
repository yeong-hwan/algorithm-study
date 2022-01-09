#include <iostream>
using namespace std;

int main()
{
  int T, N;
  int F[41] = { 0, 1 };
  
  for(int n = 2; n <= 40; n++) 
    F[n] = F[n-1] + F[n-2];

  cin >> T;
  for(int i = 0; i < T; i++)
  {
    cin >> N;
    if (N == 0) 
        cout << "1 0" << endl;

    else
        cout << F[N-1] <<  F[N] << endl;
  }
  
  return 0;
}