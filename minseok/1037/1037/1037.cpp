#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int n;
	cin >> n;
	int* input = new int[n];
	for (int i = 0; i < n; i++) {
		cin >> input[n];
	}
	sort(input, input + n);
	cout << input[0] * input[n - 1];
	return 0;
}