#include <iostream>
#include <string>
using namespace std;

int main() {
	string word;
	string alphabet = "abcdefghijklmnopqrstuvwxyz";
	cin >> word;

	for (int i = 0; i < alphabet.length(); i++) {
		cout << (int)word.find(alphabet[i]) << " ";
	}
}