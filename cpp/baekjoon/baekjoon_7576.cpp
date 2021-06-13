// v1
// # include <iostream>
// # include <queue>

// using namespace std;

// int main(){
//     cin.tie(NULL);
//     ios_base::sync_with_stdio(false);

//     int M, N, tomato_zero=0;
//     queue<pair<int, int>> que;
//     cin >> M >> N;
//     int arr[N][M] = {0};
//     for(int i=0; i<N; ++i){
//         for(int j=0; j<M; ++j){
//             cin >> arr[i][j];
//         }
//     }

//     for(int i=0; i<N; ++i){
//         for(int j=0; j<M; ++j){
//             if (arr[i][j] == 0){
//                 tomato_zero += 1;
//             }
//             if (arr[i][j] == 1){
//                 que.push({i,j});
//             }
//         }
//     }
//     int dx[4] = {0,-1,0,1};
//     int dy[4] = {-1,0,1,0};
//     int tomato_cnt = 0;
//     int s_i = 0, s_j = 0;
//     int res = 0;
//     while (!que.empty()){
//         s_i = que.front().first;
//         s_j = que.front().second;
//         que.pop();

//         for (int c=0; c<4; ++c){
//             int x = s_i + dx[c];
//             int y = s_j + dy[c];
//             if (0<=x && x<N && 0<=y && y<M){
//                 if (arr[x][y] == 0){
//                     que.push({x,y});
//                     arr[x][y] = arr[s_i][s_j] + 1;
//                     ++tomato_cnt;
//                     if (res < arr[x][y]){
//                         res = arr[x][y];
//                     }
//                 }
//             }
//         }
//     }

//     if (tomato_cnt == tomato_zero){
//         if (res == 0){
//             cout << 0 << '\n';
//         }
//         else{
//             cout << res-1 <<'\n';
//         }
//     }
//     else{
//         cout << -1 <<'\n';
//     }

// }


// v2
# include <iostream>
# include <queue>

using namespace std;

int main(){
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);

    int M, N, tomato_zero=0;
    queue<pair<int, int>> que;
    cin >> M >> N;
    int arr[N][M] = {0};
    for(int i=0; i<N; ++i){
        for(int j=0; j<M; ++j){
            cin >> arr[i][j];
            if (arr[i][j] == 0){
                tomato_zero += 1;
            }
            if (arr[i][j] == 1){
                que.push({i,j});
            }
        }
        }
    
    int dx[4] = {0,-1,0,1};
    int dy[4] = {-1,0,1,0};
    int tomato_cnt = 0;
    int s_i = 0, s_j = 0;
    int res = 0;
    while (!que.empty()){
        s_i = que.front().first;
        s_j = que.front().second;
        que.pop();

        for (int c=0; c<4; ++c){
            int x = s_i + dx[c];
            int y = s_j + dy[c];
            if (0<=x && x<N && 0<=y && y<M){
                if (arr[x][y] == 0){
                    que.push({x,y});
                    arr[x][y] = arr[s_i][s_j] + 1;
                    ++tomato_cnt;
                    if (res < arr[x][y]){
                        res = arr[x][y];
                    }
                }
            }
        }
    }

    if (tomato_cnt == tomato_zero){
        if (res == 0){
            cout << 0 << '\n';
        }
        else{
            cout << res-1 <<'\n';
        }
    }
    else{
        cout << -1 <<'\n';
    }

}

