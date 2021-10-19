// baekjoon_1854 K번째 최단 경로 찾기

//v1
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#define INF 987654321

using namespace std;

vector<pair<int, int>> adj_list[1001];

vector<vector<int>> dijkstra(int K) {
	vector<vector<int>> visited(1001, vector<int>(K, INF));
	priority_queue < pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
	pq.push({ 0, 1 });
	visited[1][0] = 0;

	while (!pq.empty()) {
		int dist = pq.top().first;
		int cur_node = pq.top().second;
		pq.pop();

		for (int i = 0; i < adj_list[cur_node].size(); ++i) {
			int next_node = adj_list[cur_node][i].first;
			int next_dist = adj_list[cur_node][i].second;
			int cost = dist + next_dist;

			if (cost < visited[next_node][K - 1]) {
				pq.push({ cost, next_node });
				visited[next_node][K - 1] = cost;
				sort(visited[next_node].begin(), visited[next_node].end());
			}
		}


	}

	return visited;
}


int main() {
	int N, M, K;
	cin >> N >> M >> K;

	int a, b, c;
	for (int m = 0; m < M; ++m) {
		cin >> a >> b >> c;
		adj_list[a].push_back({ b, c });
	}

	vector<vector<int>> visited = dijkstra(K);

	for (int i = 1; i < N + 1; ++i) {
		if (visited[i][K - 1] == INF) cout << -1 << '\n';
		else cout << visited[i][K - 1] << '\n';

	}
}