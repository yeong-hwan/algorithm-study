#include <iostream>
using namespace std;

int w(int, int, int);

int memos[21 * 21 * 21];
int main() {
  int a, b, c;

  fill_n(memos, 21 * 21 * 21, INT32_MIN);
  while (1) {
    cin >> a;
    cin >> b;
    cin >> c;
    if (a == -1 && b == -1 && c == -1)
      break;
    cout << "w(" << a << ", " << b << ", " << c << ") = " << w(a, b, c) << endl;
  }

  return 0;
}

int w(int a, int b, int c) {
  if (a <= 0 || b <= 0 || c <= 0)
    return 1;

  if (a > 20 || b > 20 || c > 20) {
    a = 20;
    b = 20;
    c = 20;
  }

  if (memos[21 * 21 * a + 21 * b + c] == INT32_MIN) {
    if (a < b && b < c) {
      memos[21 * 21 * a + 21 * b + c] =
          w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c);
    } else {
      memos[21 * 21 * a + 21 * b + c] = w(a - 1, b, c) + w(a - 1, b - 1, c) +
                                        w(a - 1, b, c - 1) -
                                        w(a - 1, b - 1, c - 1);
    }
  }
  return memos[21 * 21 * a + 21 * b + c];
}