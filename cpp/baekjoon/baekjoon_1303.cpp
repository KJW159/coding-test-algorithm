// baekjoon_1303 ¿¸≈ı


//v1
#include <iostream>
#include <queue>
#include <vector>
#include <string>
#include <cmath>

using namespace std;

vector<vector<char>> field(100);
vector<vector<int>> visited(100, vector<int>(100));
int N, M;
int dx[4] = { 0,-1,0,1 };
int dy[4] = { -1,0,1,0 };


int counting_soldier(int s_i, int s_j, char color) {
	
	int cnt = 1;
	queue<pair<int, int>> q;
	q.push({ s_i, s_j });
	visited[s_i][s_j] = 1;


	while (!q.empty()) {
		s_i = q.front().first;
		s_j = q.front().second;
		q.pop();

		for (int c = 0; c < 4; ++c) {
			int x = s_i + dx[c];
			int y = s_j + dy[c];
			if (0 <= x && x < M && 0 <= y && y < N) {
				if (visited[x][y] == 0 && field[x][y] == color) {
					visited[x][y] = 1;
					q.push({ x,y });
					cnt++;
				}
			}
		}

	}
	return cnt;
}


int main() {
	cin.tie(0);
	ios_base::sync_with_stdio(0);
	int res[2] = { 0,0 };
	cin >> N >> M;

	for (int i = 0; i < M; ++i) {
		string soldiers;
		cin >> soldiers;
		for (int j = 0; j < N; ++j) {
			field[i].push_back(soldiers[j]);
		}
	}

	for (int i = 0; i < M; ++i) {
		for (int j = 0; j < N; ++j) {
			if (visited[i][j] == 0) {
				int cnt = counting_soldier(i,j, field[i][j]);
				if (field[i][j] == 'W') {
					res[0] += pow(cnt,2);
				}
				else {
					res[1] += pow(cnt,2);
				}
			}
		}
	}
	cout << res[0] << ' ' << res[1] << '\n';

}