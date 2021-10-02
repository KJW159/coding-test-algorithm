// baekjoon_2577 숫자의 개수 세기

#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
	string res;
	int A, B, C;
	int num_computed = 1;
	vector<int> num_cnt(10);
	

	cin >> A >> B >> C;
	num_computed = A * B * C;
	res = to_string(num_computed);

	for (int i = 0; i < res.size(); ++i) {
		int idx = res[i] - '0';
		num_cnt[idx] += 1;
	}

	for (int i = 0; i < 10; ++i) {
		cout << num_cnt[i] << '\n';
	}
}