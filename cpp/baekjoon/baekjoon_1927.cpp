// v1

#include <iostream>
#include <queue>

using namespace std;

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);

    int N, num;
    priority_queue<int,vector<int>,greater<int>> pq;
    cin >> N;

    for (int i=0; i<N; ++i){
        cin >> num;
        if (num == 0){
            if(pq.empty()){
                cout << 0 << '\n';
            }
            else{
                cout << pq.top() << '\n';
                pq.pop();
            }
        }
        else{
            pq.push(num);
        }
    }

}