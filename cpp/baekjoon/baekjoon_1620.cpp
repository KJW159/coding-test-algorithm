// baekjoon_1620 나는야 포켓몬 마스터 이다솜


// v1
#include <iostream>
#include <map>
#include <cctype>
#include <string>

using namespace std;

int main() {
	cin.tie(0);
	ios_base::sync_with_stdio(0);

	int N, M;
	cin >> N >> M;

	map<string, int> dict_name;
	map<int, string> dict_num;

	string mon_name;
	for (int i = 1; i < N+1; ++i) {
		cin >> mon_name;
		dict_name[mon_name] = i;
		dict_num[i] = mon_name;
	}

	string pokemon;
	for (int i = 0; i < M; ++i) {
		cin >> pokemon;
		if (isdigit(pokemon[0])) {
			cout << dict_num[stoi(pokemon)] << '\n';
		}
		else {
			cout << dict_name[pokemon] << '\n';
		}
	}
}