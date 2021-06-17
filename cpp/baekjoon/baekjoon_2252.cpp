// baekjoon_2252 줄 세우기


#include <iostream>
#include <queue>
#include <vector>
#include <array>

using namespace std;

int main(){
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);


    int N, M, a, b;
    vector<int> res;
    vector<int> adj[32001];
    int indegree[32001] = {0};
    queue<int> q;

    cin >> N >> M;

    for (int i=0; i<M; ++i){
        cin >> a >> b;
        adj[a].push_back(b);
        indegree[b] += 1;
    }

    for (int i=1; i<N+1; ++i){
        if (indegree[i]==0){
            q.push(i);
        }
    }

    while (!q.empty()){
        int pre_man = q.front();
        q.pop();
        res.push_back(pre_man);

        for (int i=0; i<adj[pre_man].size(); ++i){
            int next_man = adj[pre_man][i];
            indegree[next_man] -= 1;
            if (indegree[next_man] == 0){
                q.push(next_man);
            }
        }
    }

    for (int i=0; i<N; ++i){
        cout << res[i] << ' ';
    }

}