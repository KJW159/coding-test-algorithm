//jungol_1620 전화번호 속의 암호


//v3
//#include <iostream>
//#include <vector>
//#include <string>
//
//using namespace std;
//
//int main() {
//	cin.tie(0);
//	ios_base::sync_with_stdio(0);
//
//	vector<string> nums;
//	string input_s;
//	int P, M;
//
//	cin >> input_s >> P >> M;
//	string num_tmp = "";
//	for (int i = 0; i < input_s.size(); ++i) {
//		if (input_s[i] != '-') {
//			num_tmp += input_s[i];
//		}
//		else {
//			nums.push_back(num_tmp);
//			num_tmp = "";
//		}
//	}
//	nums.push_back(num_tmp);
//	num_tmp = nums[M - 1];
//
//	string res = "";
//	if (num_tmp.size() > 4) {
//		res = "INPUT ERROR!";
//	}
//	else {
//		for (int i = 0; i < num_tmp.size(); ++i) {
//			int num = ((num_tmp[i] - '0') + P) % 10;
//			res += (num + '0');
//		}
//
//		if (res.size() < 4) {
//			for (int i = 0; i < 4 - res.size(); ++i) {
//				res = '0' + res;
//			}
//		}
//	}
//	cout << res << '\n';
//}


// v4
//#include <iostream>
//#include <vector>
//#include <string>
//
//using namespace std;
//
//int main() {
//	cin.tie(0);
//	ios_base::sync_with_stdio(0);
//
//	vector<string> nums;
//	string input_s;
//	int P, M;
//	string res = "";
//	cin >> input_s >> P >> M;
//	string num_tmp = "";
//	int input_size = input_s.size();
//	for (int i = 0; i < input_size; ++i) {
//		if (input_s[i] != '-') {
//			num_tmp += input_s[i];
//		}
//		else if(input_s[i] == '-' or i == input_size - 1) {
//			if (num_tmp.size() > 4) {
//				res = "INPUT ERROR!";
//				break;
//			}
//			nums.push_back(num_tmp);
//			num_tmp = "";
//		}
//	}
//
//	if (res.size() == 0) {
//		num_tmp = nums[M - 1];
//		for (int i = 0; i < num_tmp.size(); ++i) {
//			int num = ((num_tmp[i] - '0') + P) % 10;
//			res += (num + '0');
//		}
//		if (res.size() < 4) {
//			for (int i = 0; i < 4 - res.size(); ++i) {
//				res = '0' + res;
//			}
//		}
//	}
//	cout << res << '\n';
//
//}



// v5
//#include <iostream>
//#include <vector>
//#include <string>
//
//using namespace std;
//
//int main() {
//	vector<string> nums;
//	string input_s;
//	int P, M;
//	string res = "";
//
//	cin >> input_s >> P >> M;
//	string num_tmp = "";
//
//	int input_size = input_s.size();
//	for (int i = 0; i < input_size; ++i) {
//		if (input_s[i] != '-') {
//			num_tmp += input_s[i];
//		}
//		if(input_s[i] == '-' or i == input_size - 1) {
//			if (num_tmp.size() > 4) {
//				res = "INPUT ERROR!";
//				break;
//			}
//			nums.push_back(num_tmp);
//			num_tmp = "";
//		}
//	}
//
//	if (res.size() == 0) {
//		num_tmp = nums[M - 1];
//		for (int i = 0; i < num_tmp.size(); ++i) {
//			int num = ((num_tmp[i] - '0') + P) % 10;
//			res += (num + '0');
//		}
//		if (res.size() < 4) {
//			for (int i = 0; i < 4 - res.size(); ++i) {
//				res = '0' + res;
//			}
//		}
//	}
//	cout << res << '\n';
//
//}


// v6
//#include <iostream>
//#include <vector>
//#include <string>
//
//using namespace std;
//
//int main() {
//	vector<string> nums;
//	string input_s;
//	int P, M;
//	string res = "";
//
//	cin >> input_s >> P >> M;
//	string num_tmp = "";
//
//	int input_size = input_s.size();
//	for (int i = 0; i < input_size; ++i) {
//		if (input_s[i] != '-') {
//			num_tmp += input_s[i];
//		}
//		if (input_s[i] == '-' or i == input_size - 1) {
//			if (num_tmp.size() > 4) {
//				res = "INPUT ERROR!";
//				break;
//			}
//			nums.push_back(num_tmp);
//			num_tmp = "";
//		}
//	}
//	int num = 0;
//	string num_add = "";
//	if (res.empty()) {
//		num_add = nums[M - 1];
//		for (int i = 0; i < num_add.size(); ++i) {
//			num = ((num_add[i] - '0') + P) % 10;
//			res += (num + '0');
//		}
//		if (res.size() < 4) {
//			for (int i = 0; i < 4 - res.size(); ++i) {
//				res = '0' + res;
//			}
//		}
//	}
//	cout << res << '\n';
//
//}



// v7

//#include <iostream>
//#include <vector>
//#include <string>
//
//using namespace std;
//
//int main() {
//	vector<string> nums;
//	string input_s;
//	int P, M;
//	string res = "";
//
//	cin >> input_s >> P >> M;
//	string num_tmp = "";
//
//	int input_size = input_s.size();
//	for (int i = 0; i < input_size; ++i) {
//		if (input_s[i] != '-') {
//			num_tmp += input_s[i];
//		}
//		if (input_s[i] == '-' or i == input_size - 1) {
//			if (num_tmp.size() > 4) {
//				res = "INPUT ERROR!";
//				break;
//			}
//			nums.push_back(num_tmp);
//			num_tmp = "";
//		}
//	}
//	int num = 0;
//	string num_add = "";
//	if (res.empty()) {
//		num_add = nums[M - 1];
//		int num_add_size = num_add.size();
//		for (int i = 0; i < num_add_size; ++i) {
//			num = ((num_add[i] - '0') + P) % 10;
//			res += (num + '0');
//		}
//		int res_size = res.size();
//		if (res_size < 4) {
//			for (int i = 0; i < 4 - res_size; ++i) {
//				res = '0' + res;
//			}
//		}
//	}
//	cout << res << '\n';
//
//}


// v8
//#include <iostream>
//#include <vector>
//#include <string>
//
//using namespace std;
//
//int main() {
//	vector<string> nums;
//	string input_s;
//	int P, M;
//
//
//	cin >> input_s >> P >> M;
//	string num_tmp = "";
//	int trg = 0;
//	int input_size = input_s.size();
//	for (int i = 0; i < input_size; ++i) {
//		if (input_s[i] != '-') {
//			num_tmp += input_s[i];
//		}
//		if (input_s[i] == '-' or i == input_size - 1) {
//			if (num_tmp.size() > 4) {
//				trg = 1;
//				break;
//			}
//			nums.push_back(num_tmp);
//			num_tmp = "";
//		}
//	}
//	int num = 0;
//	string num_add = "";
//	string res = "";
//	if (trg == 0) {
//		num_add = nums[M - 1];
//		int num_add_size = num_add.size();
//		for (int i = 0; i < num_add_size; ++i) {
//			num = ((num_add[i] - '0') + P) % 10;
//			res += (num + '0');
//		}
//		int res_size = res.size();
//		if (res_size < 4) {
//			for (int i = 0; i < 4 - res_size; ++i) {
//				res = '0' + res;
//			}
//		}
//	}
//	if (trg == 1) cout << "INPUT ERROR!" << '\n';
//	else cout << res << '\n';
//}


// v9
//#include <iostream>
//#include <vector>
//#include <string>
//
//using namespace std;
//
//int main() {
//	vector<string> nums;
//	string input_s;
//	int P, M;
//
//
//	cin >> input_s >> P >> M;
//	string num_tmp = "";
//	int trg = 0;
//	int input_size = input_s.size();
//	for (int i = 0; i < input_size; ++i) {
//		if (input_s[i] != '-') {
//			num_tmp += input_s[i];
//		}
//		else {
//			if (num_tmp.size() > 4) {
//				trg = 1;
//				break;
//			}
//			nums.push_back(num_tmp);
//			num_tmp = "";
//		}
//	}
//	if (num_tmp.size() > 4) {
//		trg = 1;
//	}
//	nums.push_back(num_tmp);
//
//	int num = 0;
//	string num_add = "";
//	string res = "";
//	if (trg == 0) {
//		num_add = nums[M - 1];
//		int num_add_size = num_add.size();
//		for (int i = 0; i < num_add_size; ++i) {
//			num = ((num_add[i] - '0') + P) % 10;
//			res += (num + '0');
//		}
//		int res_size = res.size();
//		if (res_size < 4) {
//			for (int i = 0; i < 4 - res_size; ++i) {
//				res = '0' + res;
//			}
//		}
//	}
//	if (trg == 1) cout << "INPUT ERROR!" << '\n';
//	else cout << res << '\n';
//}


// v10
//#include <iostream>
//#include <vector>
//#include <string>
//
//using namespace std;
//
//int main() {
//	vector<string> nums;
//	string input_s;
//	int P, M;
//
//
//	cin >> input_s >> P >> M;
//	string num_tmp = "";
//	int trg = 0;
//	int input_size = input_s.size();
//	for (int i = 0; i < input_size; ++i) {
//		if (input_s[i] != '-') {
//			num_tmp += input_s[i];
//		}
//		else {
//			if (num_tmp.size() > 4) {
//				trg = 1;
//				break;
//			}
//			nums.push_back(num_tmp);
//			num_tmp = "";
//		}
//	}
//	if (num_tmp.size() > 4) {
//		trg = 1;
//	}
//	nums.push_back(num_tmp);
//
//	int num = 0;
//	string num_add = "";
//	string res = "";
//	if (trg == 0) {
//		num_add = nums[M - 1];
//		int num_add_size = num_add.size();
//		if (num_add_size < 4) {
//			for (int i = 0; i < 4 - num_add_size; ++i) {
//				num_add = '0' + num_add;
//			}
//		}
//		for (int i = 0; i < 4; ++i) {
//			num = ((num_add[i] - '0') + P) % 10;
//			res += (num + '0');
//		}
//		int res_size = res.size();
//		
//	}
//	if (trg == 1) cout << "INPUT ERROR!" << '\n';
//	else cout << res << '\n';
//}


// v11
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
	vector<string> nums;
	string input_s;
	int P, M;
	string res = "";

	cin >> input_s >> P >> M;
	string num_tmp = "";

	int input_size = input_s.size();
	for (int i = 0; i < input_size; ++i) {
		if (input_s[i] != '-') {
			num_tmp += input_s[i];
		}
		if (input_s[i] == '-' or i == input_size - 1) {
			if (num_tmp.size() > 4) {
				res = "INPUT ERROR!";
				break;
			}
			nums.push_back(num_tmp);
			num_tmp = "";
		}
	}
	int num = 0;
	string num_add = "";
	if (res.empty()) {
		num_add = nums[M - 1];
		int num_add_size = num_add.size();
		if (num_add_size < 4) {
			for (int i = 0; i < 4 - num_add_size; ++i) {
				num_add = '0' + num_add;
			}
		}

		for (int i = 0; i < 4; ++i) {
			num = ((num_add[i] - '0') + P) % 10;
			res += (num + '0');
		}

	}
	cout << res << '\n';

}