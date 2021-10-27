// baekjoon_11438 LCA2

// v1
//#include <iostream>
//#include <vector>
//#define LOG 17
//
//using namespace std;
//
//
//void dfs(int x, int cnt, vector<int>& depth, vector<vector<int>>& parents, vector<vector<int>>& adj_list) {
//
//	depth[x] = cnt;
//
//	for (int i = 0; i < adj_list[x].size(); ++i) {
//		int y = adj_list[x][i];
//		if (depth[y] == -1) {
//			// �ٷ� ������ �ִ� �θ� ����.
//			parents[y][0] = x;
//			dfs(y, cnt + 1, depth, parents, adj_list);
//		}
//	}
//}
//
//void set_parents(vector<vector<int>>& parents, int N) {
//	for (int i = 1; i <= LOG; ++i) {
//		for (int j = 1; j < N + 1; ++j) {
//			parents[j][i] = parents[parents[j][i - 1]][i - 1];
//		}
//	}
//}
//
//
//int lca(int x, int y, vector<vector<int>>& parents, vector<int>& depth) {
//	// ���� ���߱⿡ �̿��ϱ� ���ؼ� ���� ���� ����.
//	if (depth[x] < depth[y]) {
//		int tmp = y;
//		y = x;
//		x = tmp;
//	}
//	// ���� ���߱�.
//	for (int i = LOG; i >= 0; --i) {
//		if ((depth[x] - depth[y]) >= (1 << i)) {
//			x = parents[x][i];
//		}
//	}
//	if (x == y) return x;
//	// �θ� ã��
//	for (int i = LOG; i >= 0; --i) {
//		if (parents[x][i] != parents[y][i]) {
//			x = parents[x][i];
//			y = parents[y][i];
//		}
//	}
//	return parents[x][0];
//}
//
//
//int main() {
//	cin.tie(0);
//	ios_base::sync_with_stdio(0);
//
//	int N;
//	cin >> N;
//
//	vector<vector<int>> adj_list(50001);
//	vector<vector<int>> parents(50001, vector<int>(LOG + 1));
//	vector<int> depth(50001, -1);
//
//
//	int a, b;
//	for (int n = 0; n < N - 1; ++n) {
//		cin >> a >> b;
//		adj_list[a].push_back(b);
//		adj_list[b].push_back(a);
//	}
//	// ����
//	dfs(1, 0, depth, parents, adj_list);
//	// i��° �θ� ã��
//	set_parents(parents, N);
//
//	int M;
//	cin >> M;
//	for (int m = 0; m < M; ++m) {
//		cin >> a >> b;
//		cout << lca(a, b, parents, depth) << '\n';
//	}
//
//}



// v2
#include <iostream>
#include <vector>
#define LOG 17

using namespace std;


void dfs(int x, int cnt, vector<int>& depth, vector<vector<int>>& parents, vector<vector<int>>& adj_list) {

	depth[x] = cnt;

	for (int i = 0; i < adj_list[x].size(); ++i) {
		int y = adj_list[x][i];
		if (depth[y] == -1) {
			// �ٷ� ������ �ִ� �θ� ����.
			parents[y][0] = x;
			dfs(y, cnt + 1, depth, parents, adj_list);
		}
	}
}

void set_parents(vector<vector<int>>& parents, int N) {
	for (int i = 1; i <= LOG; ++i) {
		for (int j = 1; j < N + 1; ++j) {
			parents[j][i] = parents[parents[j][i - 1]][i - 1];
		}
	}
}


int lca(int x, int y, vector<vector<int>>& parents, vector<int>& depth) {
	// ���� ���߱⿡ �̿��ϱ� ���ؼ� ���� ���� ����.
	if (depth[x] < depth[y]) {
		int tmp = y;
		y = x;
		x = tmp;
	}
	// ���� ���߱�.
	for (int i = LOG; i >= 0; --i) {
		if ((depth[x] - depth[y]) >= (1 << i)) {
			x = parents[x][i];
		}
	}
	if (x == y) return x;
	// �θ� ã��
	for (int i = LOG; i >= 0; --i) {
		if (parents[x][i] != parents[y][i]) {
			x = parents[x][i];
			y = parents[y][i];
		}
	}
	return parents[x][0];
}


int main() {
	cin.tie(0);
	ios_base::sync_with_stdio(0);

	int N;
	cin >> N;

	vector<vector<int>> adj_list(100001);
	vector<vector<int>> parents(100001, vector<int>(LOG + 1));
	vector<int> depth(100001, -1);


	int a, b;
	for (int n = 0; n < N - 1; ++n) {
		cin >> a >> b;
		adj_list[a].push_back(b);
		adj_list[b].push_back(a);
	}
	// ����
	dfs(1, 0, depth, parents, adj_list);
	// i��° �θ� ã��
	set_parents(parents, N);

	int M;
	cin >> M;
	for (int m = 0; m < M; ++m) {
		cin >> a >> b;
		cout << lca(a, b, parents, depth) << '\n';
	}

}