// baekjonn_1766 문제집

//v1
// #include <iostream>
// #include <queue>
// #include <vector>
// #include <array>

// using namespace std;

// int main() {
//     cin.tie(NULL);
//     ios_base::sync_with_stdio(false);

//     int N, M, a, b;
//     vector<int> res;
//     priority_queue<int, vector<int>, greater<int>> pq;
//     vector<int> adj[32001];
//     int indegree[32001] = {0};

    
//     cin >> N >> M;

//     for (int i=0; i<M; ++i){
//         cin >> a >> b;
//         adj[a].push_back(b);
//         indegree[b] += 1;
//     }

//     for (int i=1; i<N+1; ++i){
//         if (indegree[i] == 0){
//             pq.push(i);
//         }
//     }

//     while (!pq.empty()){
//         int pre_pro = pq.top();
//         pq.pop();
//         res.push_back(pre_pro);

//         for (int i=0; i<adj[pre_pro].size(); ++i){
//             int next_pro = adj[pre_pro][i];
//             indegree[next_pro] -= 1;
//             if (indegree[next_pro] == 0){
//                 pq.push(next_pro);
//             }
//         }

//     }

//     for (int i=0; i<N; ++i){
//         cout << res[i] << ' ';
//     }

// }


// v2

#include <iostream>
#include <queue>
#include <vector>
#include <array>

using namespace std;

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);

    int N, M, a, b;
    vector<int> res;
    priority_queue<int, vector<int>, greater<int>> pq;
    int indegree[32001] = {0};

    
    cin >> N >> M;
    // vector<vector<int>> adj(N+1);
    vector<int> adj[N+1];

    for (int i=0; i<M; ++i){
        cin >> a >> b;
        adj[a].push_back(b);
        indegree[b] += 1;
    }

    for (int i=1; i<N+1; ++i){
        if (indegree[i] == 0){
            pq.push(i);
        }
    }

    while (!pq.empty()){
        int pre_pro = pq.top();
        pq.pop();
        res.push_back(pre_pro);

        for (int i=0; i<adj[pre_pro].size(); ++i){
            int next_pro = adj[pre_pro][i];
            indegree[next_pro] -= 1;
            if (indegree[next_pro] == 0){
                pq.push(next_pro);
            }
        }

    }

    for (int i=0; i<N; ++i){
        cout << res[i] << ' ';
    }

}