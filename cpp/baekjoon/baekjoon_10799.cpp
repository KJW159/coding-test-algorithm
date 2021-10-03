// baekjoon_10799 ¼è¸·´ë±â.

 
// v1
#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main() {
	int res = 0;
	stack<char> s;
	string brackets;

	cin >> brackets;
	s.push(brackets[0]);

	for (int i = 1; i < brackets.size(); ++i) {
		if (brackets[i] == '(') {
			s.push('(');
		}
		else {
			s.pop();
			if (brackets[i - 1] == '(') {
				res += s.size();
			}
			else {
				++res;
			}
		}
	}

	cout << res << '\n';
}