// baekjoon_10866 µ¦

//v1
#include <iostream>
#include <deque>
#include <string>

using namespace std;

int main() {
	cin.tie(0);
	ios_base::sync_with_stdio(0);

	int N, num;
	string order;
	deque<int> deq;

	cin >> N;
	for (int n = 0; n < N; ++n) {
		cin >> order;
		if (order == "push_back") {
			cin >> num;
			deq.push_back(num);
		}
		else if (order == "push_front") {
			cin >> num;
			deq.push_front(num);
		}
		else if (order == "pop_front") {
			if (!deq.empty()) {
				cout << deq.front() << '\n';
				deq.pop_front();
			}
			else cout << -1 << '\n';
		}
		else if (order == "pop_back") {
			if (!deq.empty()) {
				cout << deq.back() << '\n';
				deq.pop_back();
			}
			else  cout << -1 << '\n';
		}
		else if (order == "size") {
			cout << deq.size() << '\n';
		}
		else if (order == "empty") {
			if (deq.empty()) cout << 1 << '\n';
			else cout << 0 << '\n';
		}
		else if (order == "front") {
			if (!deq.empty()) cout << deq.front() << '\n';
			else cout << -1 << '\n';
		}
		else if (order == "back") {
			if (!deq.empty()) cout << deq.back() << '\n';
			else cout << -1 << '\n';
		}
	}
}
