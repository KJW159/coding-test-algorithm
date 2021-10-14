// baekjoon_1269 ´ëÄª Â÷ÁıÇÕ

// v1
#include <iostream>
#include <set>

using namespace std;

int main() {
	cin.tie(0);
	ios_base::sync_with_stdio(0);
	
	int N, M, num;
	cin >> N >> M;

	set<int> res;
	for (int i = 0; i < N; ++i) {
		cin >> num;
		res.insert(num);
	}

	for (int i = 0; i < M; ++i) {
		cin >> num;
		if (!res.count(num)) {
			res.insert(num);
		}
		else {
			res.erase(res.find(num));
		}
		
	}
	cout << res.size() << '\n';

}