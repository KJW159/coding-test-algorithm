// swea_1263  사람 네트워크

// v6

//#include <iostream>
//#include <vector>
//#include <queue>
//#define INF 987654321
//
//using namespace std;
//
//
//void bfs(int start, vector<vector<int>>& adj_list, int& res, int N) {
//	vector<int> visited(1001, INF);
//	visited[start] = 0;
//	int all_cost = 0;
//	queue<int>q;
//	q.push(start);
//
//	while (!q.empty()) {
//		int cur_node = q.front();
//		q.pop();
//		all_cost += visited[cur_node];
//
//		for (int i = 0; i < adj_list[cur_node].size(); ++i) {
//			int next_node = adj_list[cur_node][i];
//			if (visited[next_node] == INF || visited[next_node] > visited[cur_node]+1 ) {
//				q.push(next_node );
//				visited[next_node] = visited[cur_node] + 1;
//			}
//		}
//	}
//	res = min(res, all_cost);
//}
//
//
//int main() {
//	cin.tie(0);
//	ios_base::sync_with_stdio(0);
//
//	int T;
//	cin >> T;
//
//	for (int t = 1; t < T + 1; ++t) {
//		cin.tie(0);
//		ios_base::sync_with_stdio(0);
//
//		int N, res = INF;
//		cin >> N;
//		vector<vector<int>> adj_list(1001);
//
//		int edge = 0;
//		for (int i = 1; i < N + 1; ++i) {
//			for (int j = 1; j < N + 1; ++j) {
//				cin >> edge;
//				if (edge == 1) adj_list[i].push_back(j);
//			}
//		}
//		for (int n = 1; n < N + 1; ++n) {
//			bfs(n, adj_list, res, N);
//		}
//
//		cout << '#' << t << ' ' << res << '\n';
//
//	}
//}


// v7
//#include <iostream>
//#include <vector>
//#include <queue>
//#define INF 987654321
//
//using namespace std;
//
//
//void bfs(int start, vector<vector<int>>& adj_list, int& res, int N) {
//	vector<int> visited(1001, INF);
//	visited[start] = 0;
//	int all_cost = 0;
//	queue<int> q;
//	q.push(start);
//
//	while (!q.empty()) {
//		int cur_node = q.front();
//		q.pop();
//		all_cost += visited[cur_node];
//
//		if (all_cost > res) return;
//
//		for (int i = 0; i < adj_list[cur_node].size(); ++i) {
//			int next_node = adj_list[cur_node][i];
//			if (visited[next_node] == INF || visited[next_node] > visited[cur_node] + 1) {
//				q.push(next_node);
//				visited[next_node] = visited[cur_node] + 1;
//			}
//		}
//	}
//	res = min(res, all_cost);
//}
//
//
//int main() {
//	cin.tie(0);
//	ios_base::sync_with_stdio(0);
//
//	int T;
//	cin >> T;
//
//	for (int t = 1; t < T + 1; ++t) {
//		cin.tie(0);
//		ios_base::sync_with_stdio(0);
//
//		int N, res = INF;
//		cin >> N;
//		vector<vector<int>> adj_list(1001);
//
//		int edge = 0;
//		for (int i = 1; i < N + 1; ++i) {
//			for (int j = 1; j < N + 1; ++j) {
//				cin >> edge;
//				if (edge == 1) adj_list[i].push_back(j);
//			}
//		}
//		for (int n = 1; n < N + 1; ++n) {
//			bfs(n, adj_list, res, N);
//		}
//
//		cout << '#' << t << ' ' << res << '\n';
//
//	}
//}


// v8
#include <iostream>
#include <vector>
#include <queue>
#define INF 987654321

using namespace std;


void bfs(int start, vector<vector<int>>& adj_list, int& res, int N) {
	vector<int> visited(1001, INF);
	visited[start] = 0;
	int all_cost = 0;
	queue<int> q;
	q.push(start);

	while (!q.empty()) {
		int cur_node = q.front();
		q.pop();


		if (all_cost > res) return;

		for (int i = 0; i < adj_list[cur_node].size(); ++i) {
			int next_node = adj_list[cur_node][i];
			if (visited[next_node] == INF || visited[next_node] > visited[cur_node] + 1) {
				q.push(next_node);
				visited[next_node] = visited[cur_node] + 1;
				all_cost += visited[next_node];
			}
		}
	}
	res = min(res, all_cost);
}


int main() {
	cin.tie(0);
	ios_base::sync_with_stdio(0);

	int T;
	cin >> T;

	for (int t = 1; t < T + 1; ++t) {
		cin.tie(0);
		ios_base::sync_with_stdio(0);

		int N, res = INF;
		cin >> N;
		vector<vector<int>> adj_list(1001);

		int edge = 0;
		for (int i = 1; i < N + 1; ++i) {
			for (int j = 1; j < N + 1; ++j) {
				cin >> edge;
				if (edge == 1) adj_list[i].push_back(j);
			}
		}
		for (int n = 1; n < N + 1; ++n) {
			bfs(n, adj_list, res, N);
		}

		cout << '#' << t << ' ' << res << '\n';

	}
}