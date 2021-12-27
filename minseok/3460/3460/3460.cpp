#include <iostream>

using namespace std;

int main() {
	int T, n;

	cin >> T;

	for (int i = 0; i < T; i++) {
		cin >> n;
		int bin = 0;
		while (n > 0) {
			if (n % 2 == 1)
				cout << bin << " ";
			n /= 2;
			bin++;
		}
	}
}