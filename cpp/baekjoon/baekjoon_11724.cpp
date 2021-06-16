// v1

// #include <iostream>
// #include <vector>
// #include <stack>

// using namespace std;


// int main(){
//     cin.tie(NULL);
//     ios_base::sync_with_stdio(false);

//     int N, M, a, b;
//     vector<int> adj[1001];
//     int visited[1001]={0};
//     int res = 0;


//     cin >> N >> M;

//     for (int i=0; i<M; ++i){
//         cin >> a >> b;
//         adj[a].push_back(b);
//         adj[b].push_back(a);
//     }

//     stack<int> st;

//     for (int i=1; i<=N; ++i){
//         if (visited[i] == 0){
//             st.push(i);
//             visited[i] = 1;

//             while (!st.empty()){
//                 int parents = st.top();
//                 st.pop();
//                 for (int j=0; j< adj[parents].size(); ++j){
//                     int child = adj[parents][j];
//                     if (visited[child] == 0){
//                         st.push(child);
//                         visited[child] = 1;
//                     }
//                 }
//             }
//             res += 1;
//         }

//     }

//     cout << res << '\n';

// }


// v2

// #include <iostream>
// #include <vector>
// #include <stack>

// using namespace std;
// // 다른 곳에서 참조, 수정 횟수가 많으면 main함수 밖에 선언
// int visited[1001]={0};
// // 벡터를 이용하는 데 파이썬에서 리스트안에 빈 리스트 1001개 생성하는 것과 같음.
// vector<int> adj[1001];

// void dfs(int i){
//     stack<int> st;
//     st.push(i);
//     visited[i] = 1;

//     while (!st.empty()){
//         int parents = st.top();
//         st.pop();
//         for (int j=0; j< adj[parents].size(); ++j){
//             int child = adj[parents][j];
//             if (visited[child] == 0){
//                 st.push(child);
//                 visited[child] = 1;
//             }
//         }
//     }
// }

// int main(){
//     cin.tie(NULL);
//     ios_base::sync_with_stdio(false);

//     int N, M, a, b;
//     int res = 0;
//     cin >> N >> M;

//     for (int i=0; i<M; ++i){
//         cin >> a >> b;
//         adj[a].push_back(b);
//         adj[b].push_back(a);
//     }

//     for (int i=1; i<=N; ++i){
//         if (visited[i] == 0){
//             dfs(i);
//             res += 1;
//         }

//     }

//     cout << res << '\n';

// }


// re-v3

#include <iostream>
#include <stack>
#include <vector>


using namespace std;

int visited[1001] = {0};
vector<int> adj[1001];


void dfs(int start){
    stack<int> st;
    visited[start] = 1;
    st.push(start);

    while (!st.empty()){
        start = st.top();
        st.pop();

        for (int j=0; j<adj[start].size(); ++j){
            int node = adj[start][j];
            if (visited[node]==0){
                st.push(node);
                visited[node] = 1; 
            }
        }
    }
}




int main(){
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);

    int N,M,x,y,res=0;
    cin >> N >> M;
    for (int i=0; i<M; ++i){
        cin >> x >> y;
        adj[x].push_back(y);
        adj[y].push_back(x);
    }

    for (int i=1; i<N+1; ++i){
        if (visited[i]==0){
            dfs(i);
            ++res;
        }
    }

    cout << res << '\n';

}
