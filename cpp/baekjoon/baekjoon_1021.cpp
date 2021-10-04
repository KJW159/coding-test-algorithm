// baekjoon_1021 ȸ���ϴ� ť



// v1
#include <iostream>
#include <deque>
#include <vector>

using namespace std;

int main() {
	int N, M, num, res = 0;
	cin >> N >> M;
	vector<int> finding_nums;
	for (int m = 0; m < M; ++m) {
		cin >> num;
		finding_nums.push_back(num);
	}

	deque<int> deq;
	for (int i = 1; i < N + 1; ++i) {
		deq.push_back(i);
	}

	for (int m = 0; m < M; ++m) {
		int finding_num = finding_nums[m];
		// ��ġ üũ
		int position = 0;
		for (int i = 0; i < N; ++i) {
			if (deq[i] == finding_num) {
				position = i;
				break;
			}
		}
		// position >= deq.size() / 2 �� �ϸ� Ʋ��.
		if (position > deq.size() / 2) {
			while (true) {
				num = deq.front();
				if (num == finding_num) {
					deq.pop_front();
					break;
				}
				int num_tmp = deq.back();
				deq.pop_back();
				deq.push_front(num_tmp);
				res++;
			}
		}
		else {
			while (true) {
				num = deq.front();
				if (num == finding_num) {
					deq.pop_front();
					break;
				}
				deq.pop_front();
				deq.push_back(num);
				res++;
			}
		}
	}
	cout << res << '\n';
}
