// baekjoon_7785 회사에 있는 사람

// v1
#include <iostream>
#include <set>

using namespace std;

int main() {
	cin.tie(0);
	ios_base::sync_with_stdio(0);
	int N;
	cin >> N;

	string name, move;
	set<string, greater<string>>employee;

	for (int i = 0; i < N; ++i) {
		cin >> name >> move;
		if (move == "enter") {
			employee.insert(name);
		}
		else {
			employee.erase(name);
		}
	}

	for (auto it = employee.begin(); it != employee.end(); ++it) {
		cout << *it << '\n';
	}
}