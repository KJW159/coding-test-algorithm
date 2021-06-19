// baekjoon_14567 선수과목

// v1
#include <iostream>
#include <queue>
#include <array>
#include <vector>

using namespace std;

vector<int> adj[1001];
int indegree[1001] = {0};
int semester[1001] = {0};

void topology_sort(int N){
    queue<int> q;
    int pre_sub, next_sub, semester_num = 1;
    

    for (int i=1; i<N+1; ++i){
        if (indegree[i] == 0){
            q.push(i);
            semester[i] = semester_num;
        }
    }


    while (!q.empty()){
        pre_sub = q.front();
        q.pop();
        semester_num = semester[pre_sub] + 1;

        for (int i=0; i<adj[pre_sub].size(); ++i){
            next_sub = adj[pre_sub][i];
            indegree[next_sub] -= 1;
            if (indegree[next_sub] == 0){
                q.push(next_sub);
                semester[next_sub] = semester_num;
            }
        }
    }

}

int main(){
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);

    int N,M,a,b;

    cin >> N >> M;

    for (int i=0; i<M; ++i){
        cin >> a >> b;
        adj[a].push_back(b);
        indegree[b] += 1;
    }

    topology_sort(N);

    for (int i=1; i<N+1; ++i){
        cout << semester[i] << ' ';
    }

}