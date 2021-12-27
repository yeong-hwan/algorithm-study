#include <iostream>
#include <string>
using namespace std;

int main() {
	string Caesar, Origin;

	cin >> Caesar;

	for (int i = 0; i < Caesar.length(); i++) {
		if (Caesar[i] < 'D')
			Origin += Caesar[i] - 'A' + 'X';
		else
			Origin += Caesar[i] - 'D' + 'A';

	}
	cout << Origin;
}