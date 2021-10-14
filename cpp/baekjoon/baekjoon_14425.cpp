// baekjoon_14425 문자열 집합


// v1
#include <iostream>
#include <set>

using namespace std;

int main() {
	cin.tie(0);
	ios_base::sync_with_stdio(0);

	int N, M, res = 0;
	cin >> N >> M;

	string word;
	set<string> S;
	for (int i = 0; i < N; ++i) {
		cin >> word;
		S.insert(word);
	}

	for (int i = 0; i < M; ++i) {
		cin >> word;
		if (S.count(word)) {
			res++;
		}
	}
	cout << res << '\n';
}