// baekjoon_1935 ���� ǥ���2

// v1
// string���� �Է� �ް�, string ���鼭 �����ھƴ� ��쿡 �Է¹޾Ƽ� �ֱ�. 
// v1�� char�� double �������� �ٲٴ� �� �����ؼ� ���� �޴� ����� �ٲ�.

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