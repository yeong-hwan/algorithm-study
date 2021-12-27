#include <iostream>
#include <queue>
#include <string>

using namespace std;

int main() {
	int T;
	string command;
	queue<int> queue;

	cin >> T;

	for (int i = 0; i < T; i++) {
		cin >> command;

		if (command == "push") {
			int data;
			cin >> data;
			queue.push(data);
		}

		else if (command == "pop") {
			if (queue.empty()) cout << "-1" << endl;
			else {
				cout << queue.front() << endl;
				queue.pop();
			}
		}

		else if (command == "size")
			cout << queue.size() << endl;

		else if (command == "empty")
			cout << queue.empty() << endl;

		else if (command == "front") {
			if (queue.empty()) cout << "-1" << endl;
			else cout << queue.front() << endl;
		}

		else if (command == "back") {
			if (queue.empty()) cout << "-1" << endl;
			else cout << queue.back() << endl;
		}
	}
}