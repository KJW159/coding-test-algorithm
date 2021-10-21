// swea_1244 최대 상금


// v1
//#include <iostream>
//#include <vector>
//#include <string>
//#include <map>
//
//using namespace std;
//
//int res, max_cnt;
//
//void dfs(int cnt, string nums, map<pair<string, int>, int>& visited) {
//	if (cnt == max_cnt) {
//		int num_int = stoi(nums);
//		if (num_int > res) {
//			res = num_int;
//		}
//		return;
//	}
//
//	for (int i = 0; i < nums.size(); ++i) {
//		for (int j = i; j < nums.size(); ++j) {
//			char tmp = nums[i];
//			nums[i] = nums[j];
//			nums[j] = tmp;
//			if (visited.find({ nums, cnt + 1 }) == visited.end()) {
//				visited[{nums, cnt + 1}] = 1;
//				dfs(cnt + 1, nums, visited);
//			}
//			tmp = nums[i];
//			nums[i] = nums[j];
//			nums[j] = tmp;
//		}
//	}
//}
//
//
//
//int main() {
//	int T;
//	cin >> T;
//
//	for (int t = 1; t < T + 1; ++t) {
//		string nums;
//		cin >> nums >> max_cnt;
//		res = 0;
//		map<pair<string, int>, int> visited;
//		dfs(0, nums, visited);
//		cout << '#' << t << ' ' << res << '\n';
//	}
//}



// v2
//#include <iostream>
//#include <vector>
//#include <string>
//#include <map>
//
//using namespace std;
//
//int res = 0, max_cnt;
//
//void dfs(int cnt, string nums, map<pair<string, int>, int>& visited) {
//	if (cnt == max_cnt) {
//		int num_int = stoi(nums);
//		if (num_int > res) {
//			res = num_int;
//		}
//		return;
//	}
//
//	for (int i = 0; i < nums.size(); ++i) {
//		for (int j = i; j < nums.size(); ++j) {
//			char tmp = nums[i];
//			nums[i] = nums[j];
//			nums[j] = tmp;
//			if (visited.count({ nums, cnt + 1 }) == 0) {
//				visited[{nums, cnt + 1}] = 1;
//				dfs(cnt + 1, nums, visited);
//			}
//			tmp = nums[i];
//			nums[i] = nums[j];
//			nums[j] = tmp;
//		}
//	}
//}
//
//
//
//int main() {
//	int T;
//	cin >> T;
//
//	for (int t = 1; t < T + 1; ++t) {
//		string nums;
//		cin >> nums >> max_cnt;
//		res = 0;
//		map<pair<string, int>, int> visited;
//		dfs(0, nums, visited);
//		cout << '#' << t << ' ' << res << '\n';
//	}
//}



// v3
#include <iostream>
#include <vector>
#include <string>
#include <map>

using namespace std;

int res, max_cnt;

void dfs(int cnt, string nums, map<pair<string, int>, int>& visited) {
	if (cnt == max_cnt) {
		int num_int = stoi(nums);
		if (num_int > res) {
			res = num_int;
		}
		return;
	}

	for (int i = 0; i < nums.size(); ++i) {
		for (int j = i+1; j < nums.size(); ++j) {
			char tmp = nums[i];
			nums[i] = nums[j];
			nums[j] = tmp;
			if (visited.count({ nums, cnt + 1 }) == 0) {
				visited[{nums, cnt + 1}] = 1;
				dfs(cnt + 1, nums, visited);
			}
			tmp = nums[i];
			nums[i] = nums[j];
			nums[j] = tmp;
		}
	}
}



int main() {
	int T;
	cin >> T;

	for (int t = 1; t < t + 1; ++t) {
		string nums;
		cin >> nums >> max_cnt;
		res = 0;
		map<pair<string, int>, int> visited;
		dfs(0, nums, visited);
		cout << '#' << t << ' ' << res << '\n';
	}
}