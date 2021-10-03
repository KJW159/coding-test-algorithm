// baekjoon_1935 후위 표기식2

// v1
// string으로 입력 받고, string 보면서 연산자아닌 경우에 입력받아서 넣기. 
// v1은 char를 double 형식으로 바꾸는 데 복잡해서 숫자 받는 방식을 바꿈.

// v1
//#include <iostream>
//#include <string>
//#include <stack>
//
//using namespace std;
//
//int main() {
//	int N;
//	char num;
//	cin >> N;
//	string postfix;
//
//	cin >> postfix;
//	int j = 0;
//	for (int i = 0; i < N; ++i) {
//		cin >> num;
//		while (j < postfix.size()) {
//			char tmp = postfix[j];
//			if (tmp == '*' || tmp == '+' || tmp == '-' || tmp == '/') {
//				j++;
//				continue;
//			}
//			else {
//				postfix[j] = num;
//				j++;
//				break;
//			}
//		}
//	}
//
//	stack<double> s;
//	for (int i = 0; i < postfix.size(); ++i) {
//		char tmp = postfix[i];
//		if (tmp == '*' || tmp == '+' || tmp == '-' || tmp == '/') {
//			0;
//		}
//		else {
//			double nums = stod(postfix[i]);
//			s.push()
//		}
//	}
//
//
//}


// v2
#include <iostream>
#include <string>
#include <stack>
#include <vector>
#include <cctype>


using namespace std;

int main() {
	int N, num;
	cin >> N;
	string postfix;
	cin >> postfix;
	vector<int> nums(N);
	for (int i = 0; i < N; ++i) {
		cin >> nums[i];
	}

	stack<double> s;
	for (int i = 0; i < postfix.size(); ++i) {
		if (isalpha(postfix[i])) {
			s.push(nums[postfix[i] - 'A']);
		}
		else {
			double n1 = s.top(); s.pop();
			double n2 = s.top(); s.pop();
			double tmp;
			//if (postfix[i] == '*') s.push(n1 * n2);
			//else if (postfix[i] == '/') s.push(n1 / n2);
			//else if (postfix[i] == '+') s.push(n1 + n2);
			//else s.push(n1 - n2);
			if (postfix[i] == '*') s.push(n2 * n1);
			else if (postfix[i] == '/') s.push(n2 / n1);
			else if (postfix[i] == '+') s.push(n2 + n1);
			else s.push(n2 - n1);
		}
	}
	cout << fixed;
	cout.precision(2);
	cout << s.top() << '\n';
}