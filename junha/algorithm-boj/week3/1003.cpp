#include <iostream>
using namespace std;

int main(){
  int T, n;
  uint32_t cntZero[41] = {1, }, cntOne[41] = {0, 1, };

  for(int i = 2; i <= 40; i++){
    cntZero[i] += cntZero[i-2] + cntZero[i-1];
    cntOne[i] += cntOne[i-2] + cntOne[i-1];
  }

  cin >> T;
  for(int t = 0; t < T; t++){
    cin >> n;
    cout << cntZero[n] << " " << cntOne[n] << endl;
  }

  return 0;
}