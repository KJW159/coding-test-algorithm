// baekjoon_10845 ť

// v1
#include <iostream>
#include <queue>
#include <string>

using namespace std;


int main() {
	cin.tie(0);
	ios_base::sync_with_stdio(0);
	int N, num;
	string order;
	queue<int> que;
	
	cin >> N;

	for (int n = 0; n < N; ++n) {
		cin >> order;
		if (order == "push") {
			cin >> num;
			que.push(num);
		}
		else if (order == "pop") {
			if (!que.empty()) cout << que.front() << '\n', que.pop();
			else cout << -1 << '\n';
		}
		else if (order == "size") {
			cout << que.size() << '\n';
		}
		else if (order == "empty") {
			if (que.empty()) cout << 1 << '\n';
			else cout << 0 << '\n';
		}
		else if (order == "front") {
			if (!que.empty()) cout << que.front() << '\n';
			else cout << -1 << '\n';
		}
		else if (order == "back") {
			if (!que.empty()) cout << que.back() << '\n';
			else cout << -1 << '\n';
		}
	}
	
}