#include <iostream>
#include <string>
#include <deque>

using namespace std;

int main() {

	int n;
	int data;
	deque<int> DQ;
	string command;
	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> command;

		if (command == "push_front") {
			cin >> data;
			DQ.push_front(data);
		}

		else if (command == "push_back") {
			cin >> data;
			DQ.push_back(data);
		}

		else if (command == "pop_front") {
			if (DQ.empty()) cout << "-1" << endl;
			else {
				cout << DQ.front() << endl;
				DQ.pop_front();
			}
		}

		else if (command == "pop_back") {
			if (DQ.empty()) cout << "-1" << endl;
			else {
				cout << DQ.back() << endl;
				DQ.pop_back();
			}
		}

		else if (command == "size") {
			cout << DQ.size() << endl;
		}

		else if (command == "empty") {
			if (DQ.empty()) cout << 1;
			else cout << -1;
		}

		else if (command == "front") {
			if (DQ.empty()) cout << "-1" << endl;
			else cout << DQ.front();
		}

		else if (command == "back") {
			if (DQ.empty()) cout << "-1" << endl;
			else cout << DQ.back();
		}
	}
	return 0;
}