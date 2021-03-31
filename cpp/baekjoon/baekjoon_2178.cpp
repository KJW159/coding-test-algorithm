#include <iostream>
#include <queue>
#include <string>

using namespace std;

int N,M,res;
int arr[100][100] = {0};

int bfs() {
    int dx[4] = {0,-1,0,1};
    int dy[4] = {-1,0,1,0}; 
    int cnt, x,y;
    queue<pair<int,int>> que;
    que.push({0,0});
    arr[0][0] = 2;

    while (!que.empty()){
        x = que.front().first;
        y = que.front().second;
        que.pop();

        if (x==N-1 && y == M-1){
            cnt = arr[x][y];
            return cnt;
        }

        for (int c=0; c<4; ++c){
            int nx = x + dx[c];
            int ny = y + dy[c];
            if (0 <= nx && nx < N && 0 <= ny && ny < M){
                if (arr[nx][ny] == 1){
                    arr[nx][ny] = arr[x][y] + 1;
                    que.push({nx,ny});
                }
            }
        }
    }
}


int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);

    cin >> N >> M;
    for (int i=0; i<N; ++i){
        string tmp;
        cin >> tmp;
        for (int j=0; j<M; ++j){
            arr[i][j] = tmp[j]-'0';
        }
    }
    res = bfs();
    cout << res-1 << '\n';
}