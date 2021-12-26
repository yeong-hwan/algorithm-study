#include <iostream>

using namespace std;

int main() {
	int input[9];
	int MaxValue = 0, MaxIndex = 0;
	for (int i = 0; i < 9; i++) {
		cin >> input[i];
		if (MaxValue < input[i]) {
			MaxValue = input[i];
			MaxIndex = i;
		}
	}
	cout << MaxValue << endl << MaxIndex + 1;
}