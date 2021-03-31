// v1
// #include <iostream>
// #include <queue>

// using namespace std;

// struct comp {
//     bool operator()(int n1, int n2){
//         if (abs(n1)>abs(n2)){
//             return true;
//         }
//         else if (abs(n1)==abs(n2)){
//             if (n1 > n2){
//                 return true;
//             }
//             else{
//                 return false;
//             }
//         }
//         else{
//             return false;
//         }
//     }
// };


// int main() {
//     cin.tie(NULL);
//     ios_base::sync_with_stdio(false);

//     int N, num;
//     priority_queue<int, vector<int>, comp> pq;
//     cin >> N;
//     for (int i=0; i<N; ++i){
//         cin >> num;
//         if (num == 0){
//             if (pq.empty()){
//                 cout << 0 << '\n';
//             }
//             else{
//                 cout << pq.top() << '\n';
//                 pq.pop();
//             }
//         }
//         else{
//             pq.push(num);
//         }
        
//     }

// }

// v2
#include <iostream>
#include <queue>

using namespace std;


int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);

    int N, num;
    priority_queue<pair<int,int>> pq;
    cin >> N;
    for (int i=0; i<N; ++i){
        cin >> num;
        if (num == 0){
            if (pq.empty()){
                cout << 0 << '\n';
            }
            else{
                cout << -pq.top().second << '\n';
                pq.pop();
            }
        }
        else{
            pq.push({-abs(num), -num});
        }
        
    }

}