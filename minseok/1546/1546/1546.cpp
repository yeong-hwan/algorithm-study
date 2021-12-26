#include <iostream>

using namespace std;

int main() {
	int num, index;
	int Max = 0;
	float score[1000], sum = 0;

	cin >> num;

	for (int i = 0; i < num; i++) {
		cin >> score[i];
		if (Max < score[i]) {
			Max = score[i];
			index = i;
		}
	}

	for (int i = 0; i < num; i++) {
		score[i] = score[i] / Max * 100;
	}
	score[num] = Max;

	for (int i = 0; i < num; i++) {
		sum += score[i];
	}

	cout << sum / num;
}