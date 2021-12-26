#include <iostream>

using namespace std;

int main() {
	int input[7];
	int sum = 0, min = 500, cnt=0;

	for (int i = 0; i < 7; i++) {
		cin >> input[i];
		if (input[i] % 2 == 1) {
			sum += input[i];
			if (input[i] < min) {
				min = input[i];
				cnt++;
			}
		}
	}
	if (cnt == 0)
		cout << "-1";
	else
		cout << sum << endl << min;
}