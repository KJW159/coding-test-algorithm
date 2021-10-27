// swea_1251 �ϳ���


// ���� ���� long long����
// �Ÿ� L�� ����ź���� ����.

// ��� ����ؼ� ������ ����������.

// ��ǥ�� ���� �����, (����ȣ, x, y)
// 2�� for�� ���鼭 ��� ������ ����. i�� ó������ ������, j�� i ���� ����
// 


// v1
//#include <iostream>
//#include <vector>
//#include <algorithm>
//#include <cmath>
//
//
//using namespace std;
//
//
//int finding_parents(int x, vector<int>& parents) {
//  if (parents[x] != x) {
//      parents[x] = finding_parents(x, parents);
//  }
//  return parents[x];
//}
//
//void union_parents(int x, int y, vector<int>& parents) {
//  int p_x = parents[x];
//  int p_y = parents[y];
//
//  if (p_x < p_y) {
//      parents[p_y] = p_x;
//  }
//  else parents[p_x] = p_y;
//}
//
//
//
//int main() {
//  int T;
//  cin >> T;
//
//  for (int t = 1; t < T + 1; ++t) {
//      int N;
//      cin >> N;
//      vector<pair<int, int>> nodes(N + 1);
//      vector<int> parents(N + 1);
//      int x, y;
//      for (int i = 1; i < N + 1; ++i) {
//          cin >> x;
//          nodes[i].first = x;
//          parents[i] = i;
//      }
//
//      for (int i = 1; i < N + 1; ++i) {
//          cin >> y;
//          nodes[i].second = y;
//      }
//      int E;
//      cin >> E;
//      
//      vector<pair<long long, pair<int, int>>> edges;
//      
//      for (int i = 1; i < N + 1; ++i) {
//          for (int j = i+1; j < N + 1; ++j) {
//              long long cost = E * pow(abs(nodes[i].first - nodes[j].first) + abs(nodes[i].second - nodes[j].second), 2);
//              edges.push_back({ cost, {i, j} });
//          }
//      }
//
//
//
//      sort(edges.begin(), edges.end());
//      
//      int res = 0;
//      for (int i = 0; i < edges.size(); ++i) {
//          int cost = edges[i].first;
//          int a = edges[i].second.first;
//          int b = edges[i].second.second;
//
//          if (finding_parents(a, parents) != finding_parents(b, parents)) {
//              union_parents(a, b, parents);
//              res += cost;
//          }
//
//      }
//      
//      cout << '#' << t << ' ' << res << '\n';
//
//  }
//
//}


// v2

//#include <iostream>
//#include <vector>
//#include <algorithm>
//#include <cmath>
//
//
//using namespace std;
//
//
//int finding_parents(int x, vector<int>& parents) {
//    if (parents[x] != x) {
//        parents[x] = finding_parents(parents[x], parents);
//    }
//    return parents[x];
//}
//
//void union_parents(int x, int y, vector<int>& parents) {
//    int p_x = parents[x];
//    int p_y = parents[y];
//
//    if (p_x < p_y) {
//        parents[p_y] = p_x;
//    }
//    else parents[p_x] = p_y;
//}
//
//
//
//int main() {
//    int T;
//    cin >> T;
//
//    for (int t = 1; t < T + 1; ++t) {
//        int N;
//        cin >> N;
//        vector<pair<int, int>> nodes(1001);
//        vector<int> parents(1001);
//        int x, y;
//        for (int i = 1; i < N + 1; ++i) {
//            cin >> x;
//            nodes[i].first = x;
//            parents[i] = i;
//        }
//
//        for (int i = 1; i < N + 1; ++i) {
//            cin >> y;
//            nodes[i].second = y;
//        }
//        double E;
//        cin >> E;
//
//        vector<pair<long long, pair<int, int>>> edges;
//
//        for (int i = 1; i < N + 1; ++i) {
//            for (int j = i + 1; j < N + 1; ++j) {
//                long long cost = E * pow(abs(nodes[i].first - nodes[j].first) + abs(nodes[i].second - nodes[j].second), 2);
//                edges.push_back({ cost, {i, j} });
//            }
//        }
//
//
//
//        sort(edges.begin(), edges.end());
//
//        long long res = 0;
//        for (int i = 0; i < edges.size(); ++i) {
//            long long cost = edges[i].first;
//            int a = edges[i].second.first;
//            int b = edges[i].second.second;
//
//            if (finding_parents(a, parents) != finding_parents(b, parents)) {
//                union_parents(a, b, parents);
//                res += cost;
//            }
//
//        }
//
//        cout << '#' << t << ' ' << res << '\n';
//
//    }
//
//}


// v3
//#include <iostream>
//#include <vector>
//#include <algorithm>
//#include <cmath>
//
//
//using namespace std;
//
//
//int finding_parents(int x, vector<int>& parents) {
//    if (parents[x] != x) {
//        parents[x] = finding_parents(parents[x], parents);
//    }
//    return parents[x];
//}
//
//void union_parents(int x, int y, vector<int>& parents) {
//    int p_x = parents[x];
//    int p_y = parents[y];
//
//    if (p_x <= p_y) {
//        parents[p_y] = p_x;
//    }
//    else parents[p_x] = p_y;
//}
//
//
//
//int main() {
//    int T;
//    cin >> T;
//
//    for (int t = 1; t < T + 1; ++t) {
//        int N;
//        cin >> N;
//        vector<pair<long, long>> nodes(1001);
//        vector<int> parents(1001);
//        int x, y;
//        for (int i = 1; i < N + 1; ++i) {
//            cin >> x;
//            nodes[i].first = x;
//            parents[i] = i;
//        }
//
//        for (int i = 1; i < N + 1; ++i) {
//            cin >> y;
//            nodes[i].second = y;
//        }
//        double E;
//        cin >> E;
//
//        vector<pair<long long, pair<int, int>>> edges;
//
//        for (int i = 1; i < N + 1; ++i) {
//            for (int j = i + 1; j < N + 1; ++j) {
//                long long cost = E * pow(abs(nodes[i].first - nodes[j].first) + abs(nodes[i].second - nodes[j].second), 2);
//                edges.push_back({ cost, {i, j} });
//            }
//        }
//
//
//
//        sort(edges.begin(), edges.end());
//
//        long long res = 0;
//        for (int i = 0; i < edges.size(); ++i) {
//            long long cost = edges[i].first;
//            int a = edges[i].second.first;
//            int b = edges[i].second.second;
//
//            if (finding_parents(a, parents) != finding_parents(b, parents)) {
//                union_parents(a, b, parents);
//                res += cost;
//            }
//
//        }
//        cout << '#' << t << ' ' << res << '\n';
//
//    }
//}


// v4
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>


using namespace std;


int finding_parents(int x, vector<int>& parents) {
    if (parents[x] != x) {
        parents[x] = finding_parents(parents[x], parents);
    }
    return parents[x];
}

void union_parents(int x, int y, vector<int>& parents) {
    int p_x = parents[x];
    int p_y = parents[y];

    if (p_x <= p_y) {
        parents[p_y] = p_x;
    }
    else parents[p_x] = p_y;
}



int main() {
    int T;
    cin >> T;

    for (int t = 1; t < T + 1; ++t) {
        int N;
        cin >> N;
        vector<pair<long, long>> nodes(1001);
        vector<int> parents(1001);
        long long x, y;
        for (int i = 1; i < N + 1; ++i) {
            cin >> x;
            nodes[i].first = x;
            parents[i] = i;
        }

        for (int i = 1; i < N + 1; ++i) {
            cin >> y;
            nodes[i].second = y;
        }
        double E;
        cin >> E;

        vector<pair<long long, pair<int, int>>> edges;

        for (int i = 1; i < N + 1; ++i) {
            for (int j = i + 1; j < N + 1; ++j) {
                long long cost = pow(abs(nodes[i].first - nodes[j].first),2) + pow(abs(nodes[i].second - nodes[j].second), 2);
                edges.push_back({ cost, {i, j} });
            }
        }



        sort(edges.begin(), edges.end());

        long long res = 0;
        for (int i = 0; i < edges.size(); ++i) {
            long long cost = edges[i].first;
            int a = edges[i].second.first;
            int b = edges[i].second.second;

            if (finding_parents(a, parents) != finding_parents(b, parents)) {
                union_parents(a, b, parents);
                res += cost;
            }

        }
        res = round(E * res);
        cout << '#' << t << ' ' << res << '\n';

    }
}