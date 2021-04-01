#include <iostream>
#include <stack>
#include <string>
#include <queue>

using namespace std;


int arr[25][25] = {0};
int N;
int dx[4] = {0,-1,0,1};
int dy[4] = {-1,0,1,0};

int dfs(int s_i, int s_j){
    stack<pair<int, int>> st;
    int cnt_tmp = 1;
    st.push({s_i,s_j});
    arr[s_i][s_j] = 2;

    while(!st.empty()){
        s_i = st.top().first;
        s_j = st.top().second;
        st.pop();

        for (int c=0; c<4; ++c){
            int x = s_i + dx[c];
            int y = s_j + dy[c];
            if (0 <= x && x < N && 0 <= y && y <N){
                if (arr[x][y] == 1){
                    st.push({x,y});
                    arr[x][y] = 2;
                    ++cnt_tmp;
                }
            }
        }
    }
    return cnt_tmp;
}


int main(){
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);

    int res = 0;
    priority_queue<int, vector<int>, greater<int>> pq;
    cin >> N;

    for (int i=0; i<N; ++i){
        string tmp;
        cin >> tmp;
        for (int j=0; j<N; ++j){
            arr[i][j] = tmp[j]-'0';
        }
    }

    for (int i=0; i<N; ++i){
        for (int j=0; j<N; ++j){
            if (arr[i][j] == 1){
                ++res;
                pq.push(dfs(i,j));
            }
        }
    }
    cout << res << '\n';
    for (int i=0; i<res; ++i){
        cout << pq.top() << '\n';
        pq.pop();
    }
}