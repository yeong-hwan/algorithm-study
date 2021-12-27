#include <iostream>

using namespace std;

int main() {
	int n, i, j;

	cin >> n;

	for (int i = 0; i < n; i++) {
		for (int j = n; j > i; j--)
			cout << "*";
		cout << "\n";
	}
}