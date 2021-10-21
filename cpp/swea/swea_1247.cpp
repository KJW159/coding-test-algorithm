// swea_1247 최적 경로


// v1
#include <iostream>
#include <vector>

using namespace std;

int N;
int res;
int home_x, home_y;


void dfs(int cnt, int x, int y, int distance, vector<int>& visited, vector<pair<int, int>>& position) {
	if (distance > res) return;
	if (cnt == N) {
		int tmp = distance + abs(x - home_x) + abs(y - home_y);
		if (tmp < res) {
			res = tmp;
		}
		return;
	}

	for (int i = 0; i < N; ++i) {
		if (visited[i] == 0) {
			int nx = position[i].first;
			int ny = position[i].second;
			int tmp = abs(x - nx) + abs(y - ny);
			visited[i] = 1;
			dfs(cnt + 1, nx, ny, distance + tmp, visited, position);
			visited[i] = 0;
		}
	}
}




int main() {
	cin.tie(0);
	ios_base::sync_with_stdio(0);

	int T;
	cin >> T;
	for (int t = 1; t < T + 1; ++t) {
		cin >> N;
		vector<pair<int, int>> position;
		vector<int> visited(N);
		int company_x, company_y;
		cin >> company_x >> company_y >> home_x >> home_y;

		int x, y;
		for (int n = 0; n < N; ++n) {
			cin >> x >> y;
			position.push_back({ x,y });
		}
		res = 987654321;
		dfs(0, company_x, company_y, 0, visited, position);

		cout << '#' << t << ' ' << res << '\n';
	}
}
