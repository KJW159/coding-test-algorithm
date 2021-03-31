#include <iostream>
#include <queue>

using namespace std;

int main(){
    int N, num, res;
    cin >> N;
    queue<int> que;
    for (int i=1; i<=N; ++i){
        que.push(i);
    }
    while(true){
        num = que.front();
        que.pop();
        if (que.empty()){
            res = num;
            break;
        }
        num = que.front();
        que.pop();
        que.push(num);
    }
    cout << res;
}