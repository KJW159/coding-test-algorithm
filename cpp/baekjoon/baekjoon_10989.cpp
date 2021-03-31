#include <iostream>
#include <queue>

using namespace std;

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);

    int N, num;
    priority_queue<int, vector<int>, greater<int>> pq;
    cin >> N;
    for (int i=0; i<N; ++i){
        cin >> num;
        pq.push(num);
    }
    for (int i=0; i<N; ++i){
        cout << pq.top() << '\n';
        pq.pop();
    }

}