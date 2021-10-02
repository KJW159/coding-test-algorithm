// baekjoon_1919 애너그램 만들기.

// v1
//#include <iostream>
//#include <vector>
//#include <string>
//
//using namespace std;
//
//int main() {
//	string word;
//	int res = 0;
//	vector<vector<int>> word_cnt(2, vector<int>(26));
//	for (int n = 0; n < 2; ++n) {
//		cin >> word;
//		int num = 0;
//		for (int i = 0; i < word.size(); ++i) {
//			num = word[i];
//			int idx = num - 97;
//			word_cnt[n][idx] += 1;
//		}
//	}
//	for (int i = 0; i < 26; ++i) {
//		if (word_cnt[0][i] != word_cnt[1][i]) {
//			res += abs(word_cnt[0][i] - word_cnt[1][i]);
//		}
//	}
//	cout << res << '\n';
//}


// v2
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
	int res = 0;
	string A, B;
	cin >> A >> B;
	
	vector<vector<int>> word_cnt(2, vector<int>(26));
	for (int i = 0; i < A.size(); ++i){
		word_cnt[0][A[i] - 'a']++;
	}
	for (int i = 0; i < B.size(); ++i) {
		word_cnt[1][B[i] - 'a']++;
	}

	for (int i = 0; i < 26; ++i) {
		res += abs(word_cnt[0][i] - word_cnt[1][i]);
	}
	cout << res << '\n';
}