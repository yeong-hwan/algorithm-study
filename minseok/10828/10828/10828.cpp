#include <iostream>
#include <string>
#include <stack>
using namespace std;
stack<int> S;

int main() {
    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        string command;
        cin >> command;

        if (command == "push") {
            int x; 
            cin >> x;
            S.push(x);
        }

        else if (command == "top") {
            if (S.empty())cout << "-1" << endl;
            else cout << S.top() << "\n";
        }
        else if (command == "pop") {
            if (S.empty())cout << "-1" << endl;
            else {
                cout << S.top() << endl;
                S.pop();
            }
        }
        else if (command == "empty") {
            cout << S.empty() << endl;
        }
        else {
            cout << S.size() << endl;
        }
    }
    return 0;
}