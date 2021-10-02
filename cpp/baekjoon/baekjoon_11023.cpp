// baekjoon_11023 더하기3


// v1
//#include <iostream>
//#include <string>
//
//using namespace std;
//
//int main() {
//	cin.tie(0);
//	ios_base::sync_with_stdio(0);
//
//	string nums;
//	getline(cin, nums);
//	int res = 0;
//	
//	for (int i = 0; i < nums.size(); ++i) {
//		// v1,v2 둘다 입력 받은 거 끝까지 출력함.
//		// v1
//		if (nums[i] != ' ' && nums[i] != '\0') {
//		// v2
//		//if (nums[i] != ' ') {
//			res += nums[i]-'0';
//		}
//	}
//	cout << res << '\n';
//}

// v2
#include <iostream>
#include <string>

using namespace std;

int main() {
	cin.tie(0);
	ios_base::sync_with_stdio(0);
	int res=0, num;

	while (cin >> num) {
		res += num;
	}
	
	cout << res << '\n';
}