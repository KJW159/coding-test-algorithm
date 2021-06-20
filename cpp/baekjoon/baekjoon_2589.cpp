// baekjoon_2589 보물섬

#include <iostream>
#include <queue>

using namespace std;

int N, M;
int arr[50][50] = {0};
int dx[4] = {0,-1,0,1};
int dy[4] = {-1,0,1,0}; 

int bfs(int s_i, int s_j){
    int moving_time = 0;
    int visited[50][50] = {0};
    queue<pair<int, int>> q;
    
    q.push({s_i, s_j});
    visited[s_i][s_j] = 1;

    while (!q.empty()){
        s_i = q.front().first;
        s_j = q.front().second;
        q.pop();

        for (int c=0; c<4; ++c){
            int x = s_i+dx[c];
            int y = s_j+dy[c];

            if (0<=x && x<N && 0<=y && y<M){
                if (visited[x][y] ==0 && arr[x][y]==1){
                    q.push({x,y});
                    visited[x][y] = visited[s_i][s_j] + 1;
                    if (visited[x][y] > moving_time){
                        moving_time = visited[x][y];
                    }

                }
            }
        }
    }
    return moving_time;

}



int main(){
    int res=0;
    char tmp;

    cin >> N >> M;
    for (int i=0; i<N; ++i){
        for (int j=0; j<M; ++j){
            cin >> tmp;
            if (tmp == 'L'){
                arr[i][j] = 1;
            }
        }
    }
    for (int i=0; i<N; ++i){
        for (int j=0; j<M; ++j){
            if (arr[i][j] == 1){
                int res_tmp = bfs(i,j);
                if (res_tmp > res){
                    res = res_tmp;
                }
            }
        }
    }
    cout << res-1 << '\n';
}



