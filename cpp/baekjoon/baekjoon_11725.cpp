// v1
// #include <iostream>
// #include <stack>
// #include <vector>

// using namespace std;

// int main(){
//     ios_base :: sync_with_stdio(false);
//     cin.tie(NULL);
//     cout.tie(NULL);



//     int N,a,b,start,node;
//     int parents[1000000]={0};
//     vector<int> adj[1000000];
//     stack<int> stack1;


//     cin >> N;
//     for (int i=0; i<N; ++i){
//         cin >> a >> b;
//         adj[a].push_back(b);
//         adj[b].push_back(a);
//     }

//     stack1.push(1);
//     parents[1] = 1;

//     while (!stack1.empty()){
//         start = stack1.top();
//         stack1.pop();

//         for (int i=0; i < adj[start].size(); ++i){
//             node = adj[start][i];
//             if (parents[node] == 0){
//                 stack1.push(node);
//                 parents[node] = start;
//             }
//         }
//     }

//     for (int i=2; i<N+1; ++i){
//         cout << parents[i] << '\n';
//     }
//     return 0;
    
// }



// v2

# include <iostream>
# include <stack>
# include <vector>


using namespace std;

void dfs(vector<int>& parents, vector<int>& adj){
    int start;
    stack<int> stack1;
    stack1.push(1);
    parents[1] = 1;

    while (!stack1.empty()){
        start = stack1.top();
        stack1.pop();

        for (int i=0; i < adj[start].size(); ++i){
            
        }
    }

}


int main(){
    int N,a,b;
    int parents[1000000] = {0};
    vector<int> adj[1000000];

    for (int i=0; i<N; ++i){
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    dfs(parents, adj);
}