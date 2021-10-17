// baekjoon_5927 택배 배송

// v1
#include <iostream>
#include <queue>
#include <vector>
#define INF 987654321


using namespace std;

vector<int> visited(50001, INF);
vector<pair<int, int >> adj_list[50001];


void dijkstra() {
	priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
	pq.push({ 0, 1 });
	visited[1] = 0;

	while (!pq.empty()) {
		int dist = pq.top().first;
		int cur_node = pq.top().second;
		pq.pop();

		if (visited[cur_node] < dist) continue;

		for (int i = 0; i < adj_list[cur_node].size(); ++i) {
			int next_node = adj_list[cur_node][i].first;
			int next_dist = adj_list[cur_node][i].second;
			int cost = dist + next_dist;

			if (cost < visited[next_node]) {
				pq.push({ cost, next_node });
				visited[next_node] = cost;
			}
		}
	}
}


int main() {
	cin.tie(0);
	ios_base::sync_with_stdio(0);

	int N, M;
	cin >> N >> M;

	int a, b, c;
	for (int i = 0; i < M; ++i) {
		cin >> a >> b >> c;
		adj_list[a].push_back({ b,c });
		adj_list[b].push_back({ a,c });
	}

	dijkstra();

	cout << visited[N] << '\n';

}