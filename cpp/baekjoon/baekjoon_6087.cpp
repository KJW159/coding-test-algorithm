// baekjoon_6087 레이저 통신

// v1
//#include <iostream>
//#include <queue>
//#include <vector>
//#include <string>
//
//using namespace std;
//
//int W, H;
//
//int dx[4] = { 0,-1,0,1 };
//int dy[4] = { -1,0,1,0 };
//
//vector<vector<char>> field(100);
//vector<vector<int>> visited(100, vector<int>(100, 10001));
//vector<pair<int, int>> laser_position;
//
//
//
//void bfs() {
//	queue<pair<pair<int, int>, int>> q;
//	int x = laser_position[0].first;
//	int y = laser_position[0].second;
//
//	visited[x][y] = 0;
//	for (int c = 0; c < 4; ++c) {
//		int nx = x + dx[c];
//		int ny = y + dy[c];
//
//		if (0 <= nx && nx < H && 0 <= ny && ny < W) {
//			if (field[nx][ny] == '.') {
//				q.push({ { nx, ny }, c });
//				visited[nx][ny] == 0;
//			}
//		}
//	}
//
//	while (!q.empty()) {
//		x = q.front().first.first;
//		y = q.front().first.second;
//		int c = q.front().second;
//		q.pop();
//
//		for (int nc = 0; nc < 4; ++nc) {
//			int nx = x + dx[c];
//			int ny = y + dy[c];
//			if (0 <= nx && nx < H && 0 <= ny && ny < W) {
//				if (field[nx][ny] != '*') {
//					if (c != nc && visited[nx][ny] > visited[x][y] + 1) {
//						q.push({ {nx, ny}, nc });
//						visited[nx][ny] = visited[x][y] + 1;
//					}
//					else if (c == nc && visited[nx][ny] > visited[x][y]) {
//						q.push({ {nx, ny}, c });
//						visited[nx][ny] = visited[x][y];
//					}
//				}
//			}
//
//		}
//	}
//}
//
//
//int main() {
//	cin.tie(0);
//	ios_base::sync_with_stdio(0);
//	cin >> W >> H;
//
//	for (int i = 0; i < H; ++i) {
//		string field_input;
//		cin >> field_input;
//		for (int j = 0; j < W; ++j) {
//			field[i].push_back(field_input[j]);
//			if (field_input[j] == 'C') {
//				laser_position.push_back({ i,j });
//			}
//		}
//	}
//
//	bfs();
//	int end_x = laser_position[1].first;
//	int end_y = laser_position[1].second;
//
//	cout << visited[end_x][end_y] << '\n';
//}

// v2
//#include <iostream>
//#include <queue>
//#include <vector>
//#include <string>
//
//using namespace std;
//
//int W, H;
//
//int dx[4] = { 0,-1,0,1 };
//int dy[4] = { -1,0,1,0 };
//
//vector<vector<char>> field(100);
//vector<vector<int>> visited(100, vector<int>(100, 10001));
//vector<pair<int, int>> laser_position;
//
//
//
//void bfs() {
//	queue<pair<pair<int, int>, int>> q;
//	int x = laser_position[0].first;
//	int y = laser_position[0].second;
//
//	visited[x][y] = 0;
//	for (int c = 0; c < 4; ++c) {
//		int nx = x + dx[c];
//		int ny = y + dy[c];
//
//		if (0 <= nx && nx < H && 0 <= ny && ny < W) {
//			if (field[nx][ny] == '.') {
//				q.push({ { nx, ny }, c });
//				visited[nx][ny] = 0;
//			}
//		}
//	}
//
//	while (!q.empty()) {
//		x = q.front().first.first;
//		y = q.front().first.second;
//		int c = q.front().second;
//		q.pop();
//
//		for (int nc = 0; nc < 4; ++nc) {
//			int nx = x + dx[nc];
//			int ny = y + dy[nc];
//			if (0 <= nx && nx < H && 0 <= ny && ny < W) {
//				if (field[nx][ny] != '*') {
//					if (c != nc && visited[nx][ny] > visited[x][y] + 1) {
//						q.push({ {nx, ny}, nc });
//						visited[nx][ny] = visited[x][y] + 1;
//					}
//					else if (c == nc && visited[nx][ny] > visited[x][y]) {
//						q.push({ {nx, ny}, c });
//						visited[nx][ny] = visited[x][y];
//					}
//				}
//			}
//
//		}
//	}
//}
//
//
//int main() {
//	cin.tie(0);
//	ios_base::sync_with_stdio(0);
//	cin >> W >> H;
//
//	for (int i = 0; i < H; ++i) {
//		string field_input;
//		cin >> field_input;
//		for (int j = 0; j < W; ++j) {
//			field[i].push_back(field_input[j]);
//			if (field_input[j] == 'C') {
//				laser_position.push_back({ i,j });
//			}
//		}
//	}
//
//	bfs();
//	int end_x = laser_position[1].first;
//	int end_y = laser_position[1].second;
//
//	cout << visited[end_x][end_y] << '\n';
//}



// v3
//#include <iostream>
//#include <queue>
//#include <vector>
//#include <string>
//
//using namespace std;
//
//int W, H;
//
//int dx[4] = { 0,-1,0,1 };
//int dy[4] = { -1,0,1,0 };
//
//vector<vector<char>> field(100);
//vector<vector<int>> visited(100, vector<int>(100, 987654321));
//vector<pair<int, int>> laser_position;
//
//
//
//void bfs() {
//	queue<pair<pair<int, int>, int>> q;
//	int x = laser_position[0].first;
//	int y = laser_position[0].second;
//
//	visited[x][y] = 0;
//	for (int c = 0; c < 4; ++c) {
//		int nx = x + dx[c];
//		int ny = y + dy[c];
//
//		if (0 <= nx && nx < H && 0 <= ny && ny < W) {
//			if (field[nx][ny] != '*') {
//				q.push({ { nx, ny }, c });
//				visited[nx][ny] = 0;
//			}
//		}
//	}
//
//	while (!q.empty()) {
//		x = q.front().first.first;
//		y = q.front().first.second;
//		int c = q.front().second;
//		q.pop();
//
//		for (int nc = 0; nc < 4; ++nc) {
//			int nx = x + dx[nc];
//			int ny = y + dy[nc];
//			if (0 <= nx && nx < H && 0 <= ny && ny < W) {
//				if (field[nx][ny] != '*') {
//					if (c != nc && visited[nx][ny] > visited[x][y] + 1) {
//						q.push({ {nx, ny}, nc });
//						visited[nx][ny] = visited[x][y] + 1;
//					}
//					else if (c == nc && visited[nx][ny] > visited[x][y]) {
//						q.push({ {nx, ny}, c });
//						visited[nx][ny] = visited[x][y];
//					}
//				}
//			}
//
//		}
//	}
//}
//
//
//int main() {
//	cin.tie(0);
//	ios_base::sync_with_stdio(0);
//	cin >> W >> H;
//
//	for (int i = 0; i < H; ++i) {
//		string field_input;
//		cin >> field_input;
//		for (int j = 0; j < W; ++j) {
//			field[i].push_back(field_input[j]);
//			if (field_input[j] == 'C') {
//				laser_position.push_back({ i,j });
//			}
//		}
//	}
//
//	bfs();
//	int end_x = laser_position[1].first;
//	int end_y = laser_position[1].second;
//
//	cout << visited[end_x][end_y] << '\n';
//}



// v4
#include <iostream>
#include <queue>
#include <vector>
#include <string>

using namespace std;

int W, H;

int dx[4] = { 0,-1,0,1 };
int dy[4] = { -1,0,1,0 };

vector<vector<char>> field(100);
vector<vector<int>> visited(100, vector<int>(100, 987654321));
vector<pair<int, int>> laser_position;



void bfs() {
	queue<pair<pair<int, int>, pair<int, int>>> q;
	int x = laser_position[0].first;
	int y = laser_position[0].second;

	visited[x][y] = 0;
	for (int c = 0; c < 4; ++c) {
		int nx = x + dx[c];
		int ny = y + dy[c];

		if (0 <= nx && nx < H && 0 <= ny && ny < W) {
			if (field[nx][ny] != '*') {
				q.push({ { nx, ny }, {c, 0} });
				visited[nx][ny] = 0;
			}
		}
	}

	while (!q.empty()) {
		x = q.front().first.first;
		y = q.front().first.second;
		int c = q.front().second.first;
		int cnt = q.front().second.second;
		q.pop();

		for (int nc = 0; nc < 4; ++nc) {
			int nx = x + dx[nc];
			int ny = y + dy[nc];
			if (0 <= nx && nx < H && 0 <= ny && ny < W) {
				if (field[nx][ny] != '*') {
					if (c != nc && visited[nx][ny] >= cnt + 1) {
						q.push({ {nx, ny}, {nc, cnt + 1} });
						visited[nx][ny] = cnt + 1;
					}
					else if (c == nc && visited[nx][ny] > cnt) {
						q.push({ {nx, ny}, {c, cnt} });
						visited[nx][ny] = cnt;
					}
				}
			}

		}
	}
}


int main() {
	cin.tie(0);
	ios_base::sync_with_stdio(0);
	cin >> W >> H;

	for (int i = 0; i < H; ++i) {
		string field_input;
		cin >> field_input;
		for (int j = 0; j < W; ++j) {
			field[i].push_back(field_input[j]);
			if (field_input[j] == 'C') {
				laser_position.push_back({ i,j });
			}
		}
	}

	bfs();
	int end_x = laser_position[1].first;
	int end_y = laser_position[1].second;

	cout << visited[end_x][end_y] << '\n';
}