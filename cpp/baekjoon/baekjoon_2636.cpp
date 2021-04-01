#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int N, M;
int arr[100][100] = {0};
int dx[4] = {0,-1,0,1};
int dy[4] = {-1,0,1,0};
int res = 0;
int pre_cheeze_num = 0;

void bfs(vector<pair<int,int>> &melting_tmp){
    queue<pair<int, int>> que;
    int visited[100][100] = {0};

    que.push({0,0});
    visited[0][0] = 1;

    while(!que.empty()){
        int s_i = que.front().first;
        int s_j = que.front().second;
        que.pop();

        for (int c=0; c<4; ++c){
          int x = s_i + dx[c];
          int y = s_j + dy[c];

          if (0<=x && x<N && 0<=y && y<M && visited[x][y] == 0){
              if (arr[x][y]==0){
                  que.push({x,y});
                  visited[x][y] = 1;
              }
              if (arr[x][y]==1){
                  melting_tmp.push_back({x,y});
                  visited[x][y] = 1;
              }
          }
        }
    }

}


int main(){
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);


    cin >> N >> M;
    for (int i=0; i<N; ++i){
        for(int j=0; j<M; ++j){
            cin >> arr[i][j];
        }
    }

    while (true){
        vector<pair<int,int>> melting_cheezes;
        bfs(melting_cheezes);
        if (melting_cheezes.empty()){
            break;
        }
        else{
            pre_cheeze_num = melting_cheezes.size();
            ++res;
            for (int i=0; i<pre_cheeze_num; ++i){
                int c_i = melting_cheezes[i].first;
                int c_j = melting_cheezes[i].second;
                arr[c_i][c_j] = 0;
            }
        }
    }
    cout << res << '\n';
    cout << pre_cheeze_num << '\n';

}